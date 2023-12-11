import { View, Text, StyleSheet } from "react-native";
const HomeScreen = () => {
    return(
        <View style= {styles.screen}>
            <Text>This is the home screen</Text>
        </View>
    );
}

const styles = StyleSheet.create({
    screen: {
        padding : 20
    }
})
export default HomeScreen;