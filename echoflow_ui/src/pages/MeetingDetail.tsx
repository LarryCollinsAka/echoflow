import { useParams } from 'react-router-dom';

export default function MeetingDetail() {
  const { id } = useParams();
  return (
    <div style={{ padding: 32 }}>
      <h2>Meeting Details</h2>
      <div>Meeting ID: {id}</div>
      {/* TODO: Show transcript, summary, action items, etc. */}
    </div>
  );
}