import { View, Text, StyleSheet, Button } from "react-native";
import { useNavigation } from '@react-navigation/native';

const HomeScreen = () => {
    const navigation = useNavigation()
    return(
        <View style= {styles.screen}>
            <Text>This is the home screen</Text>
            <Button title = "AddIngredent" onPress={() => {navigation.navigate('AddIngredient')}}/>
        </View>
    );
}

const styles = StyleSheet.create({
    screen: {
        padding : 20
    }
})
export default HomeScreen;