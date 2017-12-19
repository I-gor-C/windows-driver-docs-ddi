---
UID: NC.vmbuskernelmodeclientlibapi.EVT_VMB_CHANNEL_SUSPEND
title: EVT_VMB_CHANNEL_SUSPEND
author: windows-driver-content
description: The EvtVmbChannelSuspend callback function is invoked at the server endpoint when the channel is being closed or deleted by the client endpoint, which moves the server into the Stopped state.
old-location: netvista\evt_vmb_channel_suspend.htm
old-project: NetVista
ms.assetid: 31FED6BE-2E89-4D36-A833-9144AD61B885
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _VIDEO_PORT_AGP_SERVICES, VIDEO_PORT_AGP_SERVICES, *PVIDEO_PORT_AGP_SERVICES, PVIDEO_PORT_AGP_SERVICES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: vmbuskernelmodeclientlibapi.h
req.include-header: VmbusKernelModeClientLibApi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFN_VMB_CHANNEL_SUSPEND
req.alt-loc: VmbusKernelModeClientLibApi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# EVT_VMB_CHANNEL_SUSPEND callback



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

The <i>EvtVmbChannelSuspend</i> callback function is invoked at the server endpoint when the channel is being
closed or deleted by the client endpoint, which moves the server into the Stopped
state.  



## -prototype

````
EVT_VMB_CHANNEL_SUSPEND EvtVmbChannelSuspend;

VOID EvtVmbChannelSuspend(
  _In_ VMBCHANNEL Channel
)
{ ... }

typedef EVT_VMB_CHANNEL_SUSPEND PFN_VMB_CHANNEL_SUSPEND;
````


## -parameters

### -param Channel [in]

The channel which is suspended.


## -returns
This callback function does not return a value.


## -remarks
After a channel is created, a client driver can specify callback functions for state changes, including  <i>EvtVmbChannelSuspend</i>, by using the <a href="netvista.vmb_channel_state_change_callbacks_init">VMB_CHANNEL_STATE_CHANGE_CALLBACKS_INIT</a> function.

If a running channel is suspended by using the <a href="netvista.vmbchannelpause">VmbChannelPause</a> function or closed by using the <a href="netvista.vmbchanneldisable">VmbChannelDisable</a> function or by the opposite endpoint, Kernel Mode Client Library (KMCL) calls <i>EvtVmbChannelSuspend</i>.  This callback guarantees that no more 
<a href="..\vmbuskernelmodeclientlibapi\nc-vmbuskernelmodeclientlibapi-evt_vmb_channel_process_packet.md">EvtVmbChannelProcessPacket</a> callbacks are running or will be queued.

<i>EvtVmbChannelSuspend</i> is also a 
notification that the KMCL client must eventually complete all outstanding 
packets indicated by using  <a href="..\vmbuskernelmodeclientlibapi\nc-vmbuskernelmodeclientlibapi-evt_vmb_channel_process_packet.md">EvtVmbChannelProcessPacket</a> These packets do 
not have to be completed synchronously.  KMCL blocks until they have 
been completed.  

The KMCL client must also stop sending packets by using the <a href="netvista.vmbpacketsend">VmbPacketSend</a>, <a href="netvista.vmbpacketsendwithexternalmdl">VmbPacketSendWithExternalMdl</a>, or <a href="netvista.vmbpacketsendwithexternalpfns">VmbPacketSendWithExternalPfns</a> functions.  



A call to <a href="netvista.vmbchannelpause">VmbChannelPause</a> on an active channel blocks until 
<i>EvtVmbChannelSuspend</i> is called and no more outstanding incoming packets exist.  
A call to <a href="netvista.vmbchanneldisable">VmbChannelDisable</a> block until the channel is paused and closed.

This function does guarantee completion of outstanding transactions.  The client may be buggy, malicious,
or the guest virtual machine may have crashed.  The server must retire any outstanding transactions, probably by cancelling them. 


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>VmbusKernelModeClientLibApi.h (include VmbusKernelModeClientLibApi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\vmbuskernelmodeclientlibapi\nc-vmbuskernelmodeclientlibapi-evt_vmb_channel_process_packet.md">EvtVmbChannelProcessPacket</a>
</dt>
<dt>
<a href="netvista.vmb_channel_state_change_callbacks_init">VMB_CHANNEL_STATE_CHANGE_CALLBACKS_INIT</a>
</dt>
<dt>
<a href="netvista.vmbchanneldisable">VmbChannelDisable</a>
</dt>
<dt>
<a href="netvista.vmbchannelpause">VmbChannelPause</a>
</dt>
<dt>
<a href="netvista.vmbpacketsend">VmbPacketSend</a>
</dt>
<dt>
<a href="netvista.vmbpacketsendwithexternalmdl">VmbPacketSendWithExternalMdl</a>
</dt>
<dt>
<a href="netvista.vmbpacketsendwithexternalpfns">VmbPacketSendWithExternalPfns</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20EVT_VMB_CHANNEL_SUSPEND callback function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

