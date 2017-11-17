---
UID: NE.wdfchildlist._WDF_RETRIEVE_CHILD_FLAGS
title: WDF_RETRIEVE_CHILD_FLAGS
author: windows-driver-content
description: The WDF_RETRIEVE_CHILD_FLAGS enumeration defines flags that a driver can set before calling WdfChildListBeginIteration.
old-location: wdf\wdf_retrieve_child_flags.htm
ms.assetid: 43294943-cc73-45d4-8e0b-e7d29420bb7e
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_RETRIEVE_CHILD_FLAGS
req.alt-loc: wdfchildlist.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: WDBGEXTS_THREAD_OS_INFO, WDBGEXTS_THREAD_OS_INFO, *PWDBGEXTS_THREAD_OS_INFO
req.iface: 
req.product: Windows 10 or later.
---

# WDF_RETRIEVE_CHILD_FLAGS enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_RETRIEVE_CHILD_FLAGS</b> enumeration defines flags that a driver can set before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545601">WdfChildListBeginIteration</a>.</p>


## -syntax

````
typedef enum _WDF_RETRIEVE_CHILD_FLAGS { 
  WdfRetrieveUnspecified      = 0x0000,
  WdfRetrievePresentChildren  = 0x0001,
  WdfRetrieveMissingChildren  = 0x0002,
  WdfRetrievePendingChildren  = 0x0004,
  WdfRetrieveAddedChildren    = (WdfRetrievePresentChildren | WdfRetrievePendingChildren),
  WdfRetrieveAllChildren      = (WdfRetrievePresentChildren | WdfRetrievePendingChildren | WdfRetrieveMissingChildren)
} WDF_RETRIEVE_CHILD_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="WdfRetrieveUnspecified"></a><a id="wdfretrieveunspecified"></a><a id="WDFRETRIEVEUNSPECIFIED"></a><b>WdfRetrieveUnspecified</b>

<dd>
<p>Reserved for internal use only.</p>
</dd>

### -field <a id="WdfRetrievePresentChildren"></a><a id="wdfretrievepresentchildren"></a><a id="WDFRETRIEVEPRESENTCHILDREN"></a><b>WdfRetrievePresentChildren</b>

<dd>
<p>Calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a> will retrieve child devices for which a framework device object exists.</p>
</dd>

### -field <a id="WdfRetrieveMissingChildren"></a><a id="wdfretrievemissingchildren"></a><a id="WDFRETRIEVEMISSINGCHILDREN"></a><b>WdfRetrieveMissingChildren</b>

<dd>
<p>Calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a> will retrieve child devices that are marked as missing. </p>
</dd>

### -field <a id="WdfRetrievePendingChildren"></a><a id="wdfretrievependingchildren"></a><a id="WDFRETRIEVEPENDINGCHILDREN"></a><b>WdfRetrievePendingChildren</b>

<dd>
<p>Calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a> will retrieve child devices that the driver has reported as present, but for which a framework device object has not been created (because the framework has not called the driver's <a href="https://msdn.microsoft.com/296fbe06-1680-43a8-b5c3-1a1faa19c6c3">EvtChildListCreateDevice</a> callback function). </p>
</dd>

### -field <a id="WdfRetrieveAddedChildren"></a><a id="wdfretrieveaddedchildren"></a><a id="WDFRETRIEVEADDEDCHILDREN"></a><b>WdfRetrieveAddedChildren</b>

<dd>
<p>Calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a> will retrieve child devices that are present or pending.</p>
</dd>

### -field <a id="WdfRetrieveAllChildren"></a><a id="wdfretrieveallchildren"></a><a id="WDFRETRIEVEALLCHILDREN"></a><b>WdfRetrieveAllChildren</b>

<dd>
<p>Calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a> will retrieve child devices that are present, pending, or missing.</p>
</dd>
</dl>

## -remarks
<p>Before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545601">WdfChildListBeginIteration</a>, your driver must set <b>WDF_RETRIEVE_CHILD_FLAGS</b>-typed flags in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551230">WDF_CHILD_LIST_ITERATOR</a> structure.</p>

<p>Before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545601">WdfChildListBeginIteration</a>, your driver must set <b>WDF_RETRIEVE_CHILD_FLAGS</b>-typed flags in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551230">WDF_CHILD_LIST_ITERATOR</a> structure.</p>

<p>Before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545601">WdfChildListBeginIteration</a>, your driver must set <b>WDF_RETRIEVE_CHILD_FLAGS</b>-typed flags in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551230">WDF_CHILD_LIST_ITERATOR</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfchildlist.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/296fbe06-1680-43a8-b5c3-1a1faa19c6c3">EvtChildListCreateDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551230">WDF_CHILD_LIST_ITERATOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545601">WdfChildListBeginIteration</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_RETRIEVE_CHILD_FLAGS enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
