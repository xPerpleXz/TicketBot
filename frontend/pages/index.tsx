import { useEffect, useState } from 'react';

export default function Home() {
  const [guilds, setGuilds] = useState([]);

  useEffect(() => {
    fetch("/api/guilds")
      .then(res => res.json())
      .then(data => setGuilds(data));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">TicketBot Dashboard</h1>
      <ul className="mt-4">
        {guilds.map((guild: any) => (
          <li key={guild.guild_id}>
            <a href={`/guilds/${guild.guild_id}`}>{guild.guild_id}</a>
          </li>
        ))}
      </ul>
    </div>
  )
}
