---
UID: NF.ks.KsEnableEvent
title: KsEnableEvent
author: windows-driver-content
description: The KsEnableEvent function enables events requested through IOCTL_KS_ENABLE_EVENT. It responds to all event identifiers defined by the sets. This function can only be called at PASSIVE_LEVEL.
old-location: stream\ksenableevent.htm
ms.assetid: 2338e583-4491-492e-b7e6-fa4e23485c22
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsEnableEvent
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
ms.keywords: KsEnableEvent
req.iface: 
---

# KsEnableEvent function



## -description
<p>The <b>KsEnableEvent</b> function enables events requested through IOCTL_KS_ENABLE_EVENT. It responds to all event identifiers defined by the sets. This function can only be called at PASSIVE_LEVEL.</p>


## -syntax

````
NTSTATUS KsEnableEvent(
  _In_           PIRP              Irp,
  _In_           ULONG             EventSetsCount,
  _In_     const KSEVENT_SET       *EventSet,
  _Inout_        PLIST_ENTRY       EventsList,
  _In_opt_       KSEVENTS_LOCKTYPE EventsFlags,
  _In_opt_       PVOID             EventsLock
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>Specifies the IRP with the enable request being handled. The file object associated with the IRP is stored with the event for later comparison when disabling the event.</p>
</dd>

### -param <i>EventSetsCount</i> [in]

<dd>
<p>Indicates the number of event set structures being passed.</p>
</dd>

### -param <i>EventSet</i> [in]

<dd>
<p>Specifies a pointer to the list of event set information.</p>
</dd>

### -param <i>EventsList</i> [in, out]

<dd>
<p>If the enabling event's KSEVENT_SET.AddHandler for the event set is <b>NULL</b>, it must point to the head of the list of KSEVENT_ENTRY items on which the event is to be added. This function assumes a single list for at least a subset of events.</p>
</dd>

### -param <i>EventsFlags</i> [in, optional]

<dd>
<p>Specifies <a href="https://msdn.microsoft.com/library/windows/hardware/ff561784">KSEVENTS_LOCKTYPE</a> flags specifying the type of exclusion lock to be used in accessing the event list, if any. If no flag is set, then no lock is taken. If a handler is specified already, this parameter is ignored.</p>
</dd>

### -param <i>EventsLock</i> [in, optional]

<dd>
<p>If the KSEVENT_SET.AddHandler for the event set containing the event being enabled is <b>NULL</b>, then this is used to synchronize access to the list. This value can be <b>NULL</b> if no flag is set in <i>EventsFlags</i>.</p>
</dd>
</dl>

## -returns
<p>The <b>KsEnableEvent</b> function returns STATUS_SUCCESS if successful, or an error specific to the event being enabled if unsuccessful. The function always sets the IO_STATUS_BLOCK.Information field of the PIRP.IoStatus element within the IRP to zero. It does not set the IO_STATUS_BLOCK.Status field, nor does it complete the IRP.</p>

## -remarks
<p>Minidrivers do not call <b>KsEnableEvent</b>. Only a pure KS driver or a class driver should call this routine.</p>

<p>Minidrivers do not call <b>KsEnableEvent</b>. Only a pure KS driver or a class driver should call this routine.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561694">KsDisableEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsEnableEvent function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
