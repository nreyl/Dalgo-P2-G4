import java.util.*;

public class P2 {

    // G es una lista de adyacencia: G[u] = arreglo con los vecinos de u
    public static int[] vecinos(int[][] G, int u) {
        return G[u];
    }

    public static int[] bfs(int[][] G, int v) {
        int n = G.length;
        Queue<Integer> cola = new LinkedList<>();
        boolean[] visitados = new boolean[n];
        int[] papas = new int[n];
        Arrays.fill(papas, -1);
        cola.offer(v);
        visitados[v] = true;
        while (!cola.isEmpty()) {
            int u = cola.poll();
            for (int vecino : vecinos(G, u)) {
                if (!visitados[vecino]) {
                    visitados[vecino] = true;
                    papas[vecino] = u;
                    cola.offer(vecino);
                }
            }
        }
        return papas;
    }

    public static void main(String[] args) {
        // Grafo del dibujo; el índice 0 no se usa para que las etiquetas coincidan (1..10)
        int[][] G = new int[11][];
        G[0] = new int[] {};
        G[1] = new int[] {2, 4};
        G[2] = new int[] {1, 3, 5, 7, 8};
        G[3] = new int[] {2, 4, 9, 10};
        G[4] = new int[] {1, 3};
        G[5] = new int[] {2, 6, 7, 8};
        G[6] = new int[] {5};
        G[7] = new int[] {2, 5, 8};
        G[8] = new int[] {2, 5, 7};
        G[9] = new int[] {3};
        G[10] = new int[] {3};

        System.out.println("papas (bfs desde 1): " + Arrays.toString(bfs(G, 1)));
    }
}
