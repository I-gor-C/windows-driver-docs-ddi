---
UID: NF.poscx.PosCxPutPendingEvent
title: PosCxPutPendingEvent
author: windows-driver-content
description: PosCxPutPendingEvent creates a new event object, copies the event data to the new event object, and tries to delegate it to the waiting caller.
old-location: pos\poscxputpendingevent.htm
ms.assetid: 4E2EA8F5-2D4A-4AEB-AF59-97D6C3FB09BC
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: pos
req.header: poscx.h
req.include-header: Poscx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PosCxPutPendingEvent
req.alt-loc: poscx.h
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
ms.keywords: PosCxPutPendingEvent
req.iface: 
req.product: Windows 10 or later.
---

# PosCxPutPendingEvent function



## -description
<p>PosCxPutPendingEvent creates a new event object, copies the event data to the
      new event object, and tries to delegate it to the waiting caller. 
      If the target caller does not have a read request waiting, the new event is added to 
      the designated event queue (control or data).</p>


## -syntax

````
NTSTATUS PosCxPutPendingEvent(
  _In_ WDFDEVICE                                  device,
  _In_ ULONG                                      deviceInterfaceTag,
  _In_ ULONG                                      eventType,
  _In_ size_t                                     rawEventDataSize,
       _In_reads_opt_(rawEventDataSize)
    PVOID rawEventDataPtr,
  _In_ POS_CX_EVENT_ATTRIBUTES                    eventAttr
);
````


## -parameters
<dl>

### -param <i>device</i> [in]

<dd>
<p>A handle to a framework device object that represents the device.</p>
</dd>

### -param <i>deviceInterfaceTag</i> [in]

<dd>
<p>The device interface associated with the event.  By default, only
          file objects that have the same tag will receive this event.</p>
</dd>

### -param <i>eventType</i> [in]

<dd>
<p>The new event type.</p>
</dd>

### -param <i>rawEventDataSize</i> [in]

<dd>
<p>The raw event (without point-of-service header) buffer size in bytes.</p>
</dd>

### -param <i>rawEventDataPtr</i> 

<dd>
<p>The pointer to the raw (without point-of-service header) event data.
          The caller may reuse/release <i>rawEventDataPtr</i> after <b>PosCxPutPendingEvent</b> returns.</p>
</dd>

### -param <i>eventAttr</i> [in]

<dd>
<p>The event attributes.</p>
</dd>
</dl>

## -returns
<p>Possible return values are:</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Product</p>
</th>
<td width="70%">
<p>Windows 10 or later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Poscx.h (include Poscx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt593142">POS_CX_EVENT_ATTRIBUTES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [pos\pos]:%20PosCxPutPendingEvent function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
