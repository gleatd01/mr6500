import asyncio
import telnetlib3
# create telnet script to connect to 192.168.1.1:5510 then run the openlock openmep etc scripts
async def shell(reader, writer):
    while True:
        # read stream until '?' mark is found
        outp = await reader.read(1024)
        if not outp:
            # End of File
            break
        elif '?' in outp:
            # reply all questions with 'y'.
            writer.write('y')

        # display all server output
        print(outp, flush=True)

    # EOF
    print()

loop = asyncio.get_event_loop()
coro = telnetlib3.open_connection('192.168.1.1', 5510, shell=shell)
reader, writer = loop.run_until_complete(coro)
loop.run_until_complete(writer.protocol.waiter_closed)