def merge_count_split_inv(arr, temp_arr, left, right):
    mid = (left + right) // 2
    i = left
    j = mid + 1
    k = left
    inv_count = 0
  
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
          
    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
  
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_count_split_inv(arr, temp_arr, left, right)
  
    return inv_count

def count_inversions(arr):
    n = len(arr)
    temp_arr = [0]*n
    return merge_sort_and_count(arr, temp_arr, 0, n - 1)

def classify_user_preference(user_order, profiles):
    min_inversions = float('inf')
    best_profile = None

    for profile_name, profile_order in profiles.items():
        mapped_order = [user_order.index(song) for song in profile_order]
        inversions = count_inversions(mapped_order)

        print(f"Inversões para {profile_name}: {inversions}")

        if inversions < min_inversions:
            min_inversions = inversions
            best_profile = profile_name

    return best_profile

# Perfis de exemplo
profiles = {
    "Pessoas que ouvem mais Pop": [
        "Blinding Lights - The Weeknd", "Levitating - Dua Lipa", "Uptown Funk - Mark Ronson ft. Bruno Mars",
        "Bad Guy - Billie Eilish", "Hotel California - Eagles", "Bohemian Rhapsody - Queen", 
        "Take Five - Dave Brubeck"
    ],
    "Pessoas que ouvem mais Rock": [
        "Bohemian Rhapsody - Queen", "Hotel California - Eagles", "Take Five - Dave Brubeck", 
        "Blinding Lights - The Weeknd", "Uptown Funk - Mark Ronson ft. Bruno Mars", 
        "Levitating - Dua Lipa", "Bad Guy - Billie Eilish"
    ],
    "Pessoas que ouvem mais Jazz": [
        "Take Five - Dave Brubeck", "Bohemian Rhapsody - Queen", "Hotel California - Eagles", 
        "Blinding Lights - The Weeknd", "Levitating - Dua Lipa", "Uptown Funk - Mark Ronson ft. Bruno Mars", 
        "Bad Guy - Billie Eilish"
    ]
}

# Listar as músicas para o usuário
musicas = [
    "Blinding Lights - The Weeknd", "Levitating - Dua Lipa", "Bohemian Rhapsody - Queen", 
    "Take Five - Dave Brubeck", "Hotel California - Eagles", "Bad Guy - Billie Eilish", 
    "Uptown Funk - Mark Ronson ft. Bruno Mars"
]

print("Aqui estão as músicas que você precisa ordenar:")
for i, musica in enumerate(musicas, 1):
    print(f"{i}. {musica}")

# Solicitar a ordenação das músicas
print("\nPor favor, insira a sua ordem preferida das músicas digitando os números correspondentes:")
user_order_indices = input("Ordem (separada por espaço, ex: 1 3 2 4 7 5 6): ").split()
user_order = [musicas[int(i) - 1] for i in user_order_indices]

# Classificar usuário
best_profile = classify_user_preference(user_order, profiles)
print(f"\nVocê pertence ao perfil: {best_profile}")
