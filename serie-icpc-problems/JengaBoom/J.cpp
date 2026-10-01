/*
    https://codeforces.com/gym/101190
    J Jenga Boom
    Angel Manuel Gonzalez Lopez
*/

// // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
#include <windows.h>
#include <psapi.h>

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

bool debug =  false;
#define DEBUG if(debug)
#define NODEBUG if(!debug)

const int MOD = 1e9 + 7;


#define YY 0
#define XX 1
#define LL 0
#define RR 1
// // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// // // // // // // // // // // // // // // // // // // // // // // // // // // // // 




// // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
// // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
int n, w, h, m; 

// 1 x // 0 y
ll cordX( int hi, int i ){
    if( hi%2 ) return 1 + 2*(i-1);
    return n; 
}
ll cordY( int hi, int i ){
    if( hi%2 )  return n;
    return 1 + 2*(i-1); 
}
ll cordXY( int hi, int i ){
    return 1 + 2*(i-1); 
}

// dado un piso saber que eje me interesa
ll queEjeMeInteresa( int hi){
    // si estamos en un pizo PAR //las fichas van a lo alrgo del eje x 
    if( hi %2 == 0 ) return YY; // me interesa cordenada en Y
    //
    // if ( hi%2 ==1 ) 
    return XX; // me interesa cordenadas en  X 
}

// debugear
// void de(   set<int> jengas[],  int cnt[], ll  sum[][2] ){
void de(  int cnt[], ll  sum[][2] ){
    for( int i=1; i<= h; i++){
        cout << " PISO " << i << " :  ";
        cout << "  cnt = " <<  cnt[i] <<  " ";
        cout << "  sumXX = " <<  sum[i][XX] <<  " ";
        cout << "  sumYY = " <<  sum[i][YY]  <<  " ";
        cout << "  elementos: ";
        // for( auto  it=jengas[i].begin(); it!=jengas[i].end(); ++it) cout << ' ' << *it; 
        cout << " \n";
    }
    cout << '\n'; 
    
}


void check_memory() {
    PROCESS_MEMORY_COUNTERS_EX pmc;
    GetProcessMemoryInfo(GetCurrentProcess(), (PROCESS_MEMORY_COUNTERS*)&pmc, sizeof(pmc));
    SIZE_T physMemUsedByMe = pmc.WorkingSetSize;
    std::cout << "Memoria usada: " << physMemUsedByMe / 1024 << " KB (" 
              << physMemUsedByMe / (1024 * 1024) << " MB)" << std::endl;
}

const int MAXH = 5000, MAXN=10000;
bool dejoDeUsar[MAXH+1][MAXN+1];



int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    ifstream cin("jenga.in");
    ofstream cout("jenga.out");


    
    cin >> n >> w; // w largo de bloques // n cantidad e bloques
    cin >> h >> m; // h altura // m bloques quitados


    // pisos pares  horizontal x  || 
    // pisos pares vertical y    =

    // para cada piso llevaamos 
    int cnt[h+2];        //  cantidad total de bloques en es episo
    ll  sum[h+1][2];       // \sum_{i=0}^n x_i   // \sum_{i=0}^n y_i 
    
    int extremos[h+1][2];
    //TODO: no ocupar ese set, hacelro con una amtriz que amruqe cuales quitaste, y lelvando left right de cada nviel


    ll suma =0;
    // for( int i=1; i<=n; i++) suma += cordenada(i);  // en mi sistema de cordenadas da siempre da n*n
    suma = n*n;


    for(int i=1; i<=h; i++){ //! O( hn )
        cnt[i] = n;
        sum[i][XX] = suma; // x
        sum[i][YY] = suma; // y
        for( int idx=1; idx<=n; idx++) dejoDeUsar[i][idx] = false;
        extremos[i][LL] = 1;
        extremos[i][RR] = n;
    }
    cnt[h+1] =0;



    DEBUG de( cnt, sum);
    // para cada bloque quitado verificamos cada nivel //! O( m h)
    int hi, idx;
    int ANS = -1;
    for( int quitar = 1; quitar<= m; quitar++ ){
        cin >> hi >> idx;
        if( ANS != -1 ) continue;
        // --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
        /// --- actualizamos el piso hi quitando el jenga (hi,idx) --- 
        cnt[hi]--;

        sum[hi][ XX ] -= cordX(hi,idx);
        sum[hi][ YY ] -= cordY(hi,idx);
        
        // si ya no hay fichas en ese piso
        if( cnt[hi] == 0 ){
            ANS = quitar;
            continue;
        }

        //  actulizar extremos      O(m) amortizado
        dejoDeUsar[hi][idx] = true;
        if( idx == extremos[hi][LL] ){
            for( int i = idx+1; i<=n; i++ ){
                if( !dejoDeUsar[hi][i] ){
                    extremos[hi][LL] =i;
                    break; // romper este for
                }
            }
        }
        if( idx == extremos[hi][RR] ){
            for( int i = idx-1; i>=0; i-- ){
                if( !dejoDeUsar[hi][i] ){
                    extremos[hi][RR] =i;
                    break; // romper este for
                }
            }
        }


        // debug
        DEBUG cout  << "\nquitamos de la altura "  << hi << " el jenga " << idx << '\n';
        DEBUG de(  cnt, sum);

        
        // --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
        
        // ----  verificamos todos los pisos // actualizando el centro de masa --- 

        // vamos acumulando el CM //   \sum_{i=0}^n x_i  / ( cantidad total de jengas  )   // cada cordenada es para X_CM y y_CM
        ll CNT = 0;    //  cantidad total de jengas 
        ll SUM[2] ={0,0};  // \sum_{i=0}^n x_i   // \sum_{i=0}^n y_i 

        DEBUG cout << "EMPEZAMOSA  VERIFICAR LOS PISOS<---\n";
        for( int piso = h-1; piso>= 1 && ANS == -1 ; piso-- ){
 
            /// actualziamos el centro de masa de todos los que etsana rriba
            CNT += cnt[ piso+1 ];
            SUM[ XX ] += sum[ piso +1 ][ XX ] ;
            SUM[ YY ] += sum[ piso +1 ][ YY ] ;

            // si no hay anda arriba
            if( CNT == 0 ) continue;

            //! como estoy revisando cuando quitamos als ficahs que ningun pisos e quede sin ficha esto nunca deberia pasar
            // / si ya no hay fichas en ese piso seguro cae
            // if( jengas[piso].begin() == jengas[piso].end() ){  // <--- ademas ya no uso el arereglod e set jengas
            //     ANS = quitar;
            //     DEBUG  cout << "sin fichas\n";
            // }

            // si tenemos almenos una ficha
            int primerIdx = extremos[piso][LL];
            int ultimoIdx = extremos[piso][RR];

            ll L = ( cordXY(piso, primerIdx ) -1) * CNT;
            ll R = ( cordXY( piso, ultimoIdx ) +1 ) * CNT;


            
            // si el centro de masa actual no esta sobre  la base del jenga 
            ll tmpsum = SUM[ queEjeMeInteresa(piso) ];
            DEBUG cout <<  "verificamos el piso " <<  piso << "  " ;
            DEBUG cout <<  "SUMXX: " << SUM[ XX ] << " SUMYY: " <<  SUM[YY] << " cnt: " << CNT << "\n";
            DEBUG cout <<  primerIdx << " < "  << " < " << ultimoIdx << "\n ";
            DEBUG cout <<  L << " < " << tmpsum << " < " << R << "\n ";
            DEBUG cout <<  L/CNT << " < " << 1.0 *tmpsum/CNT << " < " << R/CNT << "\n";

            if( !( L <  tmpsum && tmpsum < R  )  ){
                ANS = quitar;
                DEBUG cout << "no esta en base de apoyo\n";
            }
            
        }
        DEBUG cout << "TERMINAMOS DE VERIFICAR LOS PISOS<---\n";
    }


    if( ANS == -1 ) cout << "no\n";
    else{
        cout << "yes\n";
        cout << ANS << '\n';
    }
    

  
}