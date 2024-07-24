class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipeMap = {}
        for i in range(len(recipes)):
            recipeMap[recipes[i]] = ingredients[i]

        for supply in supplies:
            recipeMap[supply] = []
        
        def dfs(ingredient):
            if ingredient not in recipeMap:
                return False
            if recipeMap[ingredient] == []:
                return True

            if ingredient in visited:
                return False

            
            visited.add(ingredient)
            for ingr in recipeMap[ingredient]:
                if dfs(ingr) == False:
                    return False
            visited.remove(ingredient)
            recipeMap[ingredient] = []
            

        visited = set()
        for recipe in recipes:
            if recipe not in visited:
                dfs(recipe)
        

        res = []
        for recipe in recipes:
            if recipeMap[recipe] == []:
                res.append(recipe)

        return res



        