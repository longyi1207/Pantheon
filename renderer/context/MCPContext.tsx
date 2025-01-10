// import React, { createContext, useContext, useState } from 'react';

// interface MCPContextType {
//     activeServers: string[];
//     startServer: (serverName: string) => Promise<void>;
//     stopServer: (serverName: string) => Promise<void>;
// }

// const MCPContext = createContext<MCPContextType | undefined>(undefined);

// export const MCPProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
//     const [activeServers, setActiveServers] = useState<string[]>([]);

//     const startServer = async (serverName: string) => {
//         // Call backend API to start the server
//         const response = await fetch(`/api/mcp/start/${serverName}`, { method: 'POST' });
//         if (response.ok) {
//             setActiveServers((prev) => [...prev, serverName]);
//         } else {
//             console.error(`Failed to start server: ${serverName}`);
//         }
//     };

//     const stopServer = async (serverName: string) => {
//         // Call backend API to stop the server
//         const response = await fetch(`/api/mcp/stop/${serverName}`, { method: 'POST' });
//         if (response.ok) {
//             setActiveServers((prev) => prev.filter((name) => name !== serverName));
//         } else {
//             console.error(`Failed to stop server: ${serverName}`);
//         }
//     };

//     return (
//         <MCPContext.Provider value={{ activeServers, startServer, stopServer }}>
//             {children}
//         </MCPContext.Provider>
//     );
// };

// export const useMCP = () => {
//     const context = useContext(MCPContext);
//     if (!context) {
//         throw new Error('useMCP must be used within an MCPProvider');
//     }
//     return context;
// };
