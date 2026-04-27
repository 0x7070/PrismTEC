from datetime import datetime, timezone, timedelta

__all__ = [
    'generate_timestamp',
    'generate_iso_timestamp',
    'time_delta'
]

## REMOVE:
import pprint as p
###

## Need value checking

def generate_timestamp(timezone: timezone = timezone.utc) -> datetime:
    timezone = timezone
    current_time = datetime.now(
        tz=timezone
    )
    return current_time

def generate_iso_timestamp(reformat_suffix: bool = True,
                           timezone: timezone = timezone.utc,
                           return_conversion_dict: bool = False) -> str:
    timezone = timezone
    
    current_time = generate_timestamp(timezone=timezone)
    current_time_iso_formatted = current_time.isoformat()
    
    if reformat_suffix:
        current_time_iso_formatted = current_time_iso_formatted.replace('+00:00', 'Z')
        
    if return_conversion_dict:
        return {
            'current_time': {
                'timestamp': current_time,
                'timezone': timezone
            },
            'current_time_iso_formatted': {
                'timestamp': current_time_iso_formatted,
                'timezone': timezone
            }
        }
    
    return current_time_iso_formatted
    
# DAYS:HH:MM:SS.microseconds
def time_delta(time_a: datetime, time_b: datetime) -> None:
    time_delta = time_b - time_a
    return time_delta

if __name__ == '__main__':
    time_a = generate_timestamp()
    time_b = generate_timestamp()
    time_delta = time_delta(time_a=time_a, time_b=time_b)
    print(f'time_a: {time_a}\ntime_b: {time_b}\ntime_delta: {time_delta}')
