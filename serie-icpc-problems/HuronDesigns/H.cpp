/*
    * https://codeforces.com/gym/106540
    * H	Huron Airlines 
    * SEGUNDA FECHA mexico 2026 ICPC
    * angelmanuelgl
    * terminando de tener clara la diea y uplovear
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



struct FenwickTree {    
    vll bit;
    int n;
    FenwickTree( int n) : n(n) {
        bit.assign(n,0); // neutro max
    }
    // agregar puntual
    void add( int i, ll val){
        for( ; i<n; i = i | (i+1))
            bit[i] = max( bit[i], val);
    }
    // suuma de 0 a r
    ll sum (int r ) const{
        ll res = 0;
        for( ; r>=0 ; r = (r & (r+1)) -1  )
            res =  max(res, bit[r]);
        return res;
    }
};


const int ASIENTOS = 100005;


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

    int n; cin >> n;
    
    ll r[n], k[n];
    for(int i = 0; i < n; i++) cin >> r[i]; // fila
    for(int i = 0; i < n; i++) cin >> k[i]; // tiempo en sentarse
    
    FenwickTree tiempo_final_asiento(ASIENTOS);

    ll comeinzo_anterior = -1;
    for( int i=0; i<n; i++){
        ll libre_pasillos = tiempo_final_asiento.sum( r[i] - 1 ); // -1 por indexado en 0
        
        
        // puede salir si el anterior ya sali y espero 1s
        // y si no hay alguen antes de su fila que no se haya sentado
        ll empezar = max( libre_pasillos, comeinzo_anterior+1 );
        comeinzo_anterior = empezar;

        ll llegada = empezar + r[i];
        ll sentado = llegada + k[i];

        tiempo_final_asiento.add( r[i]-1, sentado); // indexado en 0

        DEBUG{
            cout << "pasajero " << i << " :\n";
            cout << " libre_pasillos " << libre_pasillos << "\n";
            cout << " empezar " << empezar << "\n";
            cout << " llegada " << llegada << "\n";
            cout << " sentado " << sentado << "\n\n";
        }
    }

    ll timepo_total = tiempo_final_asiento.sum( ASIENTOS-1 );
    cout << timepo_total << "\n";

    DEBUG cout << "\n\n";    
    
}