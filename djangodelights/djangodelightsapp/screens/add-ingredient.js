import { View, Text, TextInput, StyleSheet } from "react-native";

const AddIngredientScreen = () => {
    return(
        <View style= {styles.screen}>
            <Text>Add Ingredients</Text>
            <TextInput></TextInput>
            
        </View>
    );
}

const styles = StyleSheet.create({
    screen: {
        padding : 20
    }
})
export default AddIngredientScreen;