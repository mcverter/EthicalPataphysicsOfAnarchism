export const Introduction = ({french, english}) => (
 <div style={{display: 'flex', justifyContent: 'center'}}>
     <h1 style={{background: '#FAEBD7', border: '3px solid grey', padding: 12, marginRight: 10}}>Welcome to <em>{english}</em></h1>
     <h1 style={{background: '#F6F2E2', border: '3px solid grey', padding: 12, marginLeft: 10}}>Bienvenue à <em>{french}</em></h1>
 </div>
)