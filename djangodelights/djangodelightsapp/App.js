import { StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import { SafeAreaView, StyleSheet, Button, TouchableOpacity, Text, View, Platform, ScrollView, TextInput, TouchableOpacity} from 'react-native';

export default function App() {
  const [text, setText] = useState("")
  return (
    <View style = {{backgroundColor:'pink'}}>
      
      
      <SafeAreaView>
        <View>
        <Text style = {{fontSize: 55}}>Django Delights</Text>
         <Text>Platform: {Platform.OS == 'ios' ? 'ios':'android'}</Text>

        <ScrollView>
          <View style= {styles.pinkContainer}>
            <TextInput
            defaultValue={text}
            onChangeText={txt=>{setText(txt)}}
            style = {{borderWidth:1, padding:10}}/>
            
            <TouchableOpacity style={styles.btn}onPress={()=> console.log("Welcome to Django Delights!!")}>
              <Text style = {{color: 'white'}}>
                press me too
              </Text>
            </TouchableOpacity>
          </View>
        </ScrollView>
        </View>
        </SafeAreaView> 
      
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  pinkContainer : {
    backgroundColor: 'C8A2C8',
    height: 1600,
    padding: 20
  },
  btn:{
    padding: 10,
    backgroundColor: 'purple',
    width: 150,
    height: 100,
    justifyContent: 'center',
    alignItems: 'center'
  }
})