---
UID : NC:vmbuskernelmodeclientlibapi.EVT_VMB_PACKET_COMPLETION_ROUTINE
title : EVT_VMB_PACKET_COMPLETION_ROUTINE
author : windows-driver-content
description : The EvtVmbPacketCompletionRoutine callback function is invoked when the transaction associated with a sent packet is complete.
old-location : netvista\evt_vmb_packet_completion_routine.htm
old-project : netvista
ms.assetid : DEE6FBD6-4807-4216-9010-F59C9E08076B
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.evt_vmb_packet_completion_routine, EvtVmbPacketCompletionRoutine callback function [Network Drivers Starting with Windows Vista], EvtVmbPacketCompletionRoutine, EVT_VMB_PACKET_COMPLETION_ROUTINE, EVT_VMB_PACKET_COMPLETION_ROUTINE, vmbuskernelmodeclientlibapi/EvtVmbPacketCompletionRoutine, PFN_VMB_PACKET_COMPLETION_ROUTINE callback function pointer [Network Drivers Starting with Windows Vista], PFN_VMB_PACKET_COMPLETION_ROUTINE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : vmbuskernelmodeclientlibapi.h
req.include-header : VmbusKernelModeClientLibApi.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : "<=DISPATCH_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PVIDEO_PORT_AGP_SERVICES, VIDEO_PORT_AGP_SERVICES"
req.product : Windows 10 or later.
---


# EVT_VMB_PACKET_COMPLETION_ROUTINE function
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

The <i>EvtVmbPacketCompletionRoutine</i> callback function is invoked when the transaction associated with a sent packet
is complete.

## Syntax

```
EVT_VMB_PACKET_COMPLETION_ROUTINE EvtVmbPacketCompletionRoutine;

void EvtVmbPacketCompletionRoutine(
  VMBPACKET Packet,
  NTSTATUS Status,
  PVOID Buffer,
  UINT32 BufferLength
)
{...}
```

## Parameters

`Packet`

The packet that is completed.

`Status`

A status code.

`Buffer`

A buffer that contains the completion response from the opposite endpoint, if any.

`BufferLength`

Length of the <i>Buffer</i> parameter, in bytes.


## Return Value

This callback function does not return a value.

## Remarks

After allocating a packet object by using the <a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbpacketallocate.md">VmbPacketAllocate</a> function, the client drive can set a completion callback by using the <a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbpacketsetcompletionroutine.md">VmbPacketSetCompletionRoutine</a> function.  

If the sender used the VMBUS_CHANNEL_FORMAT_FLAG_WAIT_FOR_COMPLETION
flag, invocation of this callback means that the opposite endpoint received the packet and completed it.
If not, the outgoing packet was successfully placed into the ring buffer.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | vmbuskernelmodeclientlibapi.h (include VmbusKernelModeClientLibApi.h) |
| **IRQL** | "<=DISPATCH_LEVEL" |

## See Also

<a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbpacketallocate.md">VmbPacketAllocate</a>

<a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbpacketsetcompletionroutine.md">VmbPacketSetCompletionRoutine</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20EVT_VMB_PACKET_COMPLETION_ROUTINE callback function%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>