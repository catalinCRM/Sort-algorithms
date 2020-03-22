#include <iostream>
#include <fstream>
#include <time.h>
#include <chrono>
#include <algorithm>

using namespace std;
using namespace std::chrono;

void bubblesort(int v[], int n)
{
    int ok;
    int i;
    do
    {
        ok = 0;
        for(i=0; i<n-1; i++)
            if(v[i] > v[i+1])
            {
                ok = 1;
                swap(v[i], v[i+1]);
            }
        n--;

    }
    while(ok == 1);
}

///---------------------

void interclasare(int v[], int st, int dr)
{
    int i, j, k, m;
    m = (st + dr) / 2;
    int n1 = m - st + 1;
    int n2 =  dr - m;
    int v1[n1], v2[n2];
    for(i=0; i<n1; i++)
        v1[i] = v[st + i];
    for(j=0; j<n2; j++)
        v2[j] = v[m + 1+ j];
    i = 0;
    j = 0;
    k = st;
    while(i < n1 && j < n2)
    {
        if(v1[i] <= v2[j])
        {
            v[k] = v1[i];
            i++;
        }
        else
        {
            v[k] = v2[j];
            j++;
        }
        k++;
    }
    while(i < n1)
    {
        v[k] = v1[i];
        i++;
        k++;
    }
    while(j < n2)
    {
        v[k] = v2[j];
        j++;
        k++;
    }
}

void mergeSort(int v[], int st, int dr)
{
    if(st < dr)
    {
        int m = (st + dr)/2;
        mergeSort(v, st, m);
        mergeSort(v, m+1, dr);
        interclasare(v, st, dr);
    }
}

void mergeSort_r(int v[], int n)
{
    mergeSort(v, 0, n-1);
}

///---------------------

int pozitie(int v[], int st, int dr)
{
    srand(time(NULL));
    int random = st + rand() % (st - dr);
    swap(v[random], v[dr]);
    int pivot = v[dr];
    int i = (st - 1);
    for(int j=st; j<=dr - 1; j++)
    {
        if(v[j] <= pivot)
        {
            i++;
            swap(v[i], v[j]);
        }
    }
    swap(v[i + 1], v[dr]);
    return (i + 1);
}

void quick_sort(int v[], int st, int dr)
{
    if(st < dr)
    {
        int piv = pozitie(v, st, dr);
        quick_sort(v, st, piv - 1);
        quick_sort(v, piv + 1, dr);
    }
}

void quick_sort_r(int v[], int n)
{
    quick_sort(v, 0, n-1);
}

///------------------

void counting_sort(int v[], int n)
{
    int i;
    int out[n], maxim = v[0], minim = v[0];
    for(i=0; i<n; i++)
    {
        if(v[i] > maxim)
            maxim = v[i];
        if(v[i] < minim)
            minim = v[i];
    }
    int fr[maxim + 1] = {0};
    for(i=0; i<n; i++)
        fr[v[i]]++;
    for(i=0; i<maxim; i++)
        fr[i+1] += fr[i];
    for(i=maxim; i>0; i--)
        fr[i] = fr[i-1];
    fr[0] = 0;
    int a[n];
    for(i=0; i<n; i++)
    {
        a[fr[v[i]]] = v[i];
        fr[v[i]]++;
    }
    for(i=0; i<n; i++)
        v[i] = a[i];
}

///-----------------------

void cnt(int v[], int n, int exp)
{
    int output[n];
    int i, numara[10] = {0};
    for (i=0; i<n; i++)
        numara[(v[i]/exp)%10]++;
    for (i=1; i<10; i++)
        numara[i] += numara[i-1];
    for (i=n-1; i>=0; i--)
    {
        output[numara[(v[i]/exp)%10]-1] = v[i];
        numara[(v[i]/exp)%10]--;
    }
    for (i=0; i<n; i++)
        v[i] = output[i];
}

void radixsort(int v[], int n)
{
    int maxim = v[0];
    for (int i=1; i<n; i++)
        if (v[i] > maxim)
            maxim = v[i];
    for (int k=1; maxim/k>0; k*=10)
        cnt(v, n, k);
}

///--------------------------

void tester(void(*f)(int v[], int n), int v2[], int n)
{
    auto start = high_resolution_clock::now();
    f(v2, n);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    cout<<duration.count();
}

void copiaza_vector(int v2[],int v[], int n)
{
    for ( int i = 0; i < n; i++ )
        v2[i] = v[i];
}

int main()
{
    ifstream f("date.in");
    int n, max;
    cout<<"n = ";
    cin>>n;
    cout<<"maxim = ";
    cin>>max;
    int v[n];
    srand(time(NULL));
    for(int i=0; i<n; i++)
    {
        int random = rand() % max + 1;
        v[i] = random;
    }
    int v2[n];

    cout<<"Bubble Sort : ";
    copiaza_vector(v2, v, n);
    tester(bubblesort, v2, n);
    cout<<endl;

    cout<<"Merge Sort : ";
    copiaza_vector(v2, v, n);
    tester(mergeSort_r, v2, n);
    cout<<endl;

    cout<<"Quick Sort : ";
    copiaza_vector(v2, v, n);
    tester(quick_sort_r, v2, n);
    cout<<endl;

    cout<<"Counting Sort : ";
    copiaza_vector(v2, v, n);
    tester(counting_sort, v2, n);
    cout<<endl;

    cout<<"Radix Sort : ";
    copiaza_vector(v2, v, n);
    tester(radixsort, v2, n);
    cout<<endl;

    return 0;
}
