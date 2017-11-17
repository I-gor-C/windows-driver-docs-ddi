---
UID: NF.ks.KsEnableEventWithAllocator
title: KsEnableEventWithAllocator
author: windows-driver-content
description: The KsEnableEventWithAllocator function enables events requested through IOCTL_KS_ENABLE_EVENT but also allows an optional allocator callback to be used to provide a buffer for the parameters.
old-location: stream\ksenableeventwithallocator.htm
ms.assetid: ec017e5c-1c26-426d-935f-7a554d3db915
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
req.alt-api: KsEnableEventWithAllocator
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
ms.keywords: KsEnableEventWithAllocator
req.iface: 
---

# KsEnableEventWithAllocator function



## -description
<p>The <b>KsEnableEventWithAllocator</b> function enables events requested through IOCTL_KS_ENABLE_EVENT but also allows an optional allocator callback to be used to provide a buffer for the parameters. It responds to all event identifiers defined by the sets. This function can only be called at PASSIVE_LEVEL.</p>
<p>If used, the filter may need to free the buffer in some nonconventional manner. Note that the IRP_BUFFERED_IO and IRP_DEALLOCATE_BUFFER flags are not set when using a custom allocator.</p>


## -syntax

````
NTSTATUS KsEnableEventWithAllocator(
  _In_           PIRP              Irp,
  _In_           ULONG             EventSetsCount,
  _In_     const KSEVENT_SET       *EventSet,
  _Inout_        PLIST_ENTRY       EventsList,
  _In_opt_       KSEVENTS_LOCKTYPE EventsFlags,
  _In_opt_       PVOID             EventsLock,
  _In_opt_       PFNKSALLOCATOR    Allocator,
  _In_opt_       ULONG             EventItemSize
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

### -param <i>Allocator</i> [in, optional]

<dd>
<p>Optionally points to an allocation function that will be used to allocate memory to store the event parameters.</p>
</dd>

### -param <i>EventItemSize</i> [in, optional]

<dd>
<p>Optionally contains the size of each KSEVENT_ITEM structure in each list of events. The event item may be extended in order to store private information. If this parameter is zero, the structure size is assumed to be normal. If it is greater than or equal to an event item structure, the KSEVENT_ITEM_IRP_STORAGE macro can be used to return a pointer to the event item so the custom data can be retrieved. On 64-bit platforms, this parameter must be a multiple of 8.</p>
</dd>
</dl>

## -returns
<p>Same as <b>KsEnableEvent</b>, which returns STATUS_SUCCESS if successful, or an error specific to the event being enabled if unsuccessful. The function always sets the IO_STATUS_BLOCK.Information field of the PIRP.IoStatus element within the IRP to zero. It does not set the IO_STATUS_BLOCK.Status field, nor does it complete the IRP.</p>

## -remarks
<p>If the optional allocator callback is used, the filter may need to free the buffer in some nonconventional manner. Note that the IRP_BUFFERED_IO and IRP_DEALLOCATE_BUFFER flags are not set when using a custom allocator.</p>

<p>If the optional allocator callback is used, the filter may need to free the buffer in some nonconventional manner. Note that the IRP_BUFFERED_IO and IRP_DEALLOCATE_BUFFER flags are not set when using a custom allocator.</p>

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