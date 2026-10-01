/*     
    * 2025 ICPC Gran Premio de Mexico 1ra Fecha
    * H. Huron Designs
    * https://codeforces.com/gym/105873/problem/H
    * 8vo problema en dificultad
    * Probabilidad: calculo de E[ g(X)] /  DP / bitmask
    * angelmanuelgl 
    
    * Observaciones: la dificultad es puramente teorica, la implementacion es trivial
    * usar teorema de Ley del estadístico inconscient 
    * solo es definicion esperanza, ponerlo como integral de lebesgue y teo de cambio de variable
*/

#include<bits/stdc++.h>
using namespace std;

typedef int64_t ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;

#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define sz(x) (int)(x).size()

#ifdef LOCAL
    bool debug = true;
#else
    bool debug = false;
#endif

#define DEBUG if(debug)
#define NODEBUG if(!debug)

const int MOD = 1e9 + 7;


// OPERACIONES BITS
#define is_on(S,j) (S & (1 << (j)) )
#define set_bit(S,j) ( S |= (1 << (j)) )
#define clear_bit(S,j) ( S &= ~(1 << (j)) )



//  INFORMACION
int n;
const int MAXN = 21;
ll d[MAXN]; //deadline
ll p[MAXN]; //ganancia
ll c[MAXN]; //duracion
ll lx[MAXN], rx[MAXN]; // distribucion bonus U[lx,rx]
ll ly[MAXN], ry[MAXN]; // distribucion hora limite U[ly,ry]



// calcular formula a mano de E[ p_i +  X_i  * 1_{ t < Y_i  } ]
// X dist uniforme(lx_i  , rx_i ) 
// Y dist uniforme(ly_i , ry_i )
// hint: linealidad / indepenndecia / g(y) = 1_{ t < y } 
double valEsperadoGanancia( int i, ll hora){
    double gananciaMedia = 0.5* (lx[i] + rx[i]);
    
    if( hora  <= ly[i] ){
        // DEBUG cout << " caso left\n";
        return 1.0 * p[i] + gananciaMedia;
    } 

    if( ly[i] < hora && hora < ry[i] ){
        // DEBUG cout << "caso centro\n";

        double valEsp = 1.0 * p[i];

        valEsp += gananciaMedia * (ry[i] - hora) / (ry[i] - ly[i]);
        return valEsp;
    }
    
    // ry[i] <= hora 
    // DEBUG cout << " caso right\n";
    return  1.0 * p[i];
}


ll tiempoNecesario( int mask ){
    ll ans = 0;
    for(  int i=0; i<n; i++){
        if( is_on(mask, i) )
            ans += c[i];
    }
    return ans;
}

// dp[mask] = ganancia maxima al haber hecho las tareas de mask
double dp[ 1 << MAXN ]; 
double dpcheck [ 1 << MAXN ] ={}; // si ya se calculo dp[mask]

double dpfunc( int mask ){
    if( dpcheck[mask] ) return 1.0 * dp[mask];
    dpcheck[mask] = true;


    DEBUG cout << "calculado dp[ " << bitset<3>(mask) << "]\n";

    ll tiempo = tiempoNecesario(mask);
    DEBUG cout << " tiempo: " << tiempo << '\n';

    DEBUG cout << " dependencias:\n";
    double ans = 0.0;
    for( int i=0; i<n; i++){
        // si tengo que hacer esa tarea
        if( is_on(mask, i) ){

            int prevMask = mask; clear_bit(prevMask, i);
            DEBUG cout << "  " << bitset<3>(prevMask) ;

            // si puedo hacerla
            if(  d[i]  >= tiempo ){
                // hago la tarea i, y la acabo en el momento {tiempo}
                


                double valEspGan_prev = valEsperadoGanancia(i, tiempo);
                
                double posans =  dp[ prevMask ] + valEspGan_prev;
                ans = max( ans ,  posans );

                
                DEBUG cout << ": " <<valEspGan_prev << "\n";
            }

            DEBUG cout << "\n";
        }
    }

    DEBUG cout << " resultado:" << ans <<  "\n\n";

    dp[mask] = ans;
    return ans;
}


// // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// uso :  g++ -DLOCAL K.cpp
int main(){
    #ifdef LOCAL
        ifstream cin("in.txt");
    #else
        ios_base::sync_with_stdio(0); 
        cin.tie(0);
        cout.tie(0);
    #endif

    // input
    cin >> n;
    for( int i = 0; i < n; i++){
        cin >> d[i] >> p[i] >> c[i] >> lx[i] >> rx[i] >> ly[i] >> ry[i];
    }
    
    // calcular el maximo de todos los posibles subconjutnos de tareas
    double ans = 0.0;
    for( int mask=0; mask < (1 << n) ; mask++ ){
        double posans  = dpfunc(mask);
        ans = max( ans, posans);
        // DEBUG cout << " dp[ " << bitset<4>(mask ) << " ] = " << posans << '\n';
    }


    cout << fixed << setprecision(10)  << ans << '\n';
}