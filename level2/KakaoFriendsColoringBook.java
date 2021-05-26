import java.util.*;

class Solution {
    public int recur(int r, int c, boolean[][] v, int[][] p) {
        if (v[r][c]) {
            return 0;
        }
        
        v[r][c] = true;

        int val = 1;
        if (r > 0             && p[r][c] == p[r-1][c]) val += recur(r-1, c, v, p);
        if (r < p.length-1    && p[r][c] == p[r+1][c]) val += recur(r+1, c, v, p);
        if (c > 0             && p[r][c] == p[r][c-1]) val += recur(r, c-1, v, p);
        if (c < p[0].length-1 && p[r][c] == p[r][c+1]) val += recur(r, c+1, v, p);
        return val;
    }
    
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        
        boolean[][] visited = new boolean[m][n];
        for (int i = 0 ; i < m ; i++) {
            for (int j = 0 ; j < n ; j++) {
                if (picture[i][j] == 0) visited[i][j] = true;
                else                    visited[i][j] = false;
            }
        }
        
        for(int i = 0 ; i < picture.length ; i++) {
            for (int j = 0 ; j < picture[0].length ; j++) {
                if (!visited[i][j]) numberOfArea++;
                int ret = recur(i, j, visited, picture);
                if (maxSizeOfOneArea < ret)
                    maxSizeOfOneArea = ret;
            }
        }
        
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        
        return answer;
    }
}
