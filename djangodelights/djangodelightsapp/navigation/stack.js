import { createStackNavigator } from '@react-navigation/stack';
import AddIngredientScreen from '../screens/add-ingredient';
import HomeScreen from '../screens/home-screen';


const Stack = createStackNavigator();

export const HomeStack = () => {
    return (
            <Stack.Navigator>
              <Stack.Screen name="Home" component={HomeScreen}/>
              <Stack.Screen name= "AddIngredient" component= {AddIngredientScreen}/>
            </Stack.Navigator>       
    );
}
