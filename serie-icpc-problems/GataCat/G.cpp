#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

typedef int64_t ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<pii> vpii;
typedef vector<vll> vpll;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

#define fi first
#define se second
#define all(x) (x).begin, (x).end()
#define sz(x) (int)(x).size()
#define pb push_back
mt19937_64 gen(chrono::steady_clock::now().time_since_epoch().count());
uniform_int_distribution<ll> distr(1, LLONG_MAX);

template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p){
    return os << '(' << p.fi << ", " << p.se << ')';
}

template<typename C, typename T = typename enable_if<!is_same<C, string>::value, typename C::value_type>::type>
ostream& operator<<(ostream &os, const C &v){
    string sep;
    for(const T &x : v) os << sep << x, sep = " ";
    return os;
}

#define PRINT(...) logger(#__VA_ARGS__, __VA_ARGS__)

template<typename ...Args>
void logger(string vars, Args&&... values){
    cout << "[Debug]\n\t" << vars << " = ";
    string d = "[";
    (..., (cout << d << values, d = "] ["));
    cout << "\n";
}

const int MOD = 1e9 + 7;

#define MAXL 145  // el  143 es puamente empiritco
#define DEBUG if(false)

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);



    int t; cin >> t;

    // CAT[i] = cantidad de CAT en  C(AT)^i
    // GATA[i] = cantidad de GATA en  C(AT)^i
    ll CAT[MAXL], GATA[MAXL];
    CAT[0] = GATA[0] = 0;

    ll lolCAT = 0, lolGATA=0;
    for( int i=1; i<MAXL; i++){
        CAT[i] = CAT[i-1] + i ;// debe dar num trianuglares
        
        GATA[i] = GATA[i-1] + i*(i-1) / 2; // Fe // tambien hay formula cerrada peor x


        // DEBUG cout <<  i << " GATA = " << GATA[i] << " CAT = "<<  CAT[i] << "\n";
        // lolCAT += CAT[i];
        // lolGATA += GATA[i];

        // lolCAT += CAT[i];
        // if( lolCAT > 1e6 && lolGATA > 1e6 ){
        //      cout << "----------\n";
        // }

        // DEBUG cout <<  i << " acum GATA = " << lolGATA << " acum CAT = " << lolCAT << "\n";
    }
     DEBUG cout << CAT[0] << ' ' << CAT[1] << ' ' << CAT[2] << '\n';
     DEBUG cout << GATA[0] << GATA[1] << GATA[2] << '\n';
     
    while( t-- ){
        ll g,c; cin >> g >> c;
        
        if( g == 0 &&  c == 0){
            cout << "CA\n";
            continue;
        }
        
        bool algun = false;
        DEBUG cout << "caso : " << g << ' ' << c << '\n';
        for(int i=MAXL-1; i>=1 ; i-- ){ 
            int cnt = 0;
            while( c >= CAT[i]  ){
                DEBUG cout << "i"<< i;
                cout << "C";
                DEBUG cout << c;
                c= c- CAT[i];
                DEBUG cout << c ;
                cnt ++;
            }
            int cnt2 = 0;
            while( g >= GATA[i] && i>=2){
                cout << "G";
                g= g- GATA[i];
                cnt2++;
            }
            if( cnt2 > 0 || cnt >0 || algun){
                algun = true;
                cout <<"AT";
            }
        }
        cout << "\n";
        
    }

    
}
