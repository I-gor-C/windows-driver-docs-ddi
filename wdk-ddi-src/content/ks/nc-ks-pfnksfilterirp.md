---
UID: NC.ks.PFNKSFILTERIRP
title: PFNKSFILTERIRP
author: windows-driver-content
description: An AVStream minidriver's AVStrMiniFilterClose routine is called when a filter is closed. It usually is provided by minidrivers that want to free the context and resources associated with the filter.
old-location: stream\avstrminifilterclose.htm
old-project: stream
ms.assetid: f0e5b141-620d-419d-a139-ad7f9bc1e349
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: AVStrMiniFilterClose
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
req.irql: PASSIVE_LEVEL (See Remarks section)
req.iface: 
---

# PFNKSFILTERIRP callback



## -description
<p>An AVStream minidriver's <i>AVStrMiniFilterClose</i> routine is called when a filter is closed. It usually is provided by minidrivers that want to free the context and resources associated with the filter.</p>


## -prototype

````
PFNKSFILTERIRP AVStrMiniFilterClose;

NTSTATUS AVStrMiniFilterClose(
  _In_ PKSFILTER Filter,
  _In_ PIRP      Irp
)
{ ... }
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>Pointer to the <a href="..\ks\ns-ks--ksfilter.md">KSFILTER</a> structure that was just closed.</p>
</dd>

### -param <i>Irp</i> [in]

<dd>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a> for the filter.</p>
</dd>
</dl>

## -returns
<p>Return STATUS_SUCCESS or STATUS_PENDING. If a minidriver returns STATUS_PENDING, AVStream will not complete the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a> immediately. Before returning STATUS_PENDING, however, the minidriver must call <a href="..\wdm\nf-wdm-iomarkirppending.md">IoMarkIrpPending</a>. Once the processing of the close is complete, the minidriver must set the IRP's status code and then call <a href="..\ks\nf-ks-kscompletependingrequest.md">KsCompletePendingRequest</a>.</p>

## -remarks
<p>The minidriver specifies this routine's address in the <b>Close</b> member of its <a href="..\ks\ns-ks--ksfilter-dispatch.md">KSFILTER_DISPATCH</a> structure.</p>

<p>At the point at which the routine is called, any registered events on the filter have been freed, but the object is otherwise intact.</p>

<p>This routine is called at IRQL = PASSIVE_LEVEL with the device mutex held. For more information about mutexes, see <a href="NULL">Mutexes in AVStream</a>.</p>

<p>This routine is optional.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL (See Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\ns-ks--ksfilter-dispatch.md">KSFILTER_DISPATCH</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iomarkirppending.md">IoMarkIrpPending</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kscompletependingrequest.md">KsCompletePendingRequest</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20AVStrMiniFilterClose routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
