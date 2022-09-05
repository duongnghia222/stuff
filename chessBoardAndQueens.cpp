#include<iostream>
#include<vector>
#include<string>
#include<iomanip>
#include<algorithm>
#include<stdlib.h>
#include<math.h>
#include <numeric>
using namespace std;
#define ll long long
//#define N 4
vector<vector<int> > result;
bool solveUtil(vector<vector<int>> board, int n, int col);
vector<vector<int>> NQ(int n) {
	vector<vector<int>> board(n,vector<int>(n,0));
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			char c;
			cin >> c;
			if (c == '*') {
				board[i][j] = 1;
			}
		}
	}
	
	if (solveUtil(board, n, 0) == false) {
		return {};
	}
 
	sort(result.begin(), result.end());
	return result;
}
bool isSafe(vector<vector<int>> board, int row, int col, int n) {
	if (board[row][col] == 1)
	{
		return false;
	}
	for (size_t i = 0; i < col; i++)
	{
		if (board[row][i] == 2) return 0;
	}
	for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
		if (board[i][j] == 2) return 0;
	}
	for (int i = row,  j = col; (i < n) && (j >=0); i++, j--) {
		if (board[i][j] == 2) return 0;
	}
	return 1;
}
bool solveUtil(vector<vector<int>> board, int n, int col) {
	int N = board.size();
	if (col == N) {
		vector<int> v;
		for (size_t i = 0; i < n; i++)
		{
			for (size_t j = 0; j < n; j++)
			{
				if (board[i][j] == 2) {
					
					v.push_back( j);
					
				}
			}
 
		}
		result.push_back(v);
		return 1;
	}
 
	bool res = 0;
	for (size_t i = 0; i < n; i++)
	{
		if (isSafe(board, i, col, n)) {
			board[i][col] = 2;
			res = solveUtil(board, n, col + 1) || res;
			
			board[i][col] = 0;
		}
	}
	return res;
}
int main() {
	int n = 8;
	//cin >> n;
	vector<vector<int> > v = NQ(n);
	cout << v.size();
	
 
	return 0;
 
}