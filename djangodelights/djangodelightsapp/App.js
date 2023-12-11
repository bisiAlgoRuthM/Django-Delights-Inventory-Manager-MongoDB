import { NavigationContainer } from '@react-navigation/native';
import {StyleSheet} from 'react-native';
import { HomeStack } from './navigation/stack';
import { AppRegistry } from 'react-native';

export default function App() {
  return (
    <NavigationContainer>
      <HomeStack/>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  pinkContainer : {
    backgroundColor: '#C8A2C8',
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
AppRegistry.registerComponent('App', () => App)