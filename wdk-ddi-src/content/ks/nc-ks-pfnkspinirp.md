---
UID: NC.ks.PFNKSPINIRP
title: PFNKSPINIRP
author: windows-driver-content
description: An AVStream minidriver's AVStrMiniPinClose routine is called when a pin is closed. It usually is provided by minidrivers that want to free the context and resources associated with the pin.
old-location: stream\avstrminipinclose.htm
old-project: stream
ms.assetid: 8dd56703-0c22-49db-a7c0-808dfcaaf623
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AVStrMiniPinClose
req.alt-loc: ks.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
---

# PFNKSPINIRP callback



## -description
An AVStream minidriver's <i>AVStrMiniPinClose</i> routine is called when a pin is closed. It usually is provided by minidrivers that want to free the context and resources associated with the pin.



## -prototype

````
PFNKSPINIRP AVStrMiniPinClose;

NTSTATUS AVStrMiniPinClose(
  _In_ PKSPIN Pin,
  _In_ PIRP   Irp
)
{ ... }
````


## -parameters

### -param Pin [in]

Pointer to the <a href="stream.kspin">KSPIN</a> that was just closed.


### -param Irp [in]

Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a> for <i>Pin</i>.


## -returns
Return STATUS_SUCCESS or STATUS_PENDING. If a minidriver returns STATUS_PENDING, AVStream will not complete the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a> immediately. Before returning STATUS_PENDING, however, the minidriver must call <a href="kernel.iomarkirppending">IoMarkIrpPending</a>. Once the processing of the close is complete, the minidriver must set the IRP's status code and then call <a href="stream.kscompletependingrequest">KsCompletePendingRequest</a>.


## -remarks
The minidriver specifies this routine's address in the <b>Close</b> member of its <a href="stream.kspin_dispatch">KSPIN_DISPATCH</a> structure.

At the point at which the routine is called, any registered events on the pin have been freed, but the object is otherwise intact.

The filter control mutex is held while in this function. For more information about mutexes, please see <a href="https://msdn.microsoft.com/011edaaa-7449-41c3-8cfb-0d319901af8b">Mutexes in AVStream</a>.

This routine is optional.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.kspin_dispatch">KSPIN_DISPATCH</a>
</dt>
<dt>
<a href="kernel.iomarkirppending">IoMarkIrpPending</a>
</dt>
<dt>
<a href="stream.kscompletependingrequest">KsCompletePendingRequest</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20AVStrMiniPinClose routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

