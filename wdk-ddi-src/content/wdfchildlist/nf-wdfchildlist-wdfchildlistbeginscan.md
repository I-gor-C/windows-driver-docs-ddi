---
UID: NF.wdfchildlist.WdfChildListBeginScan
title: WdfChildListBeginScan
author: windows-driver-content
description: The WdfChildListBeginScan method prepares a specified list of child devices so the driver can update the information in the list.
old-location: wdf\wdfchildlistbeginscan.htm
ms.assetid: 08951cde-d9d2-4de6-bb63-7c3e7cf1f92f
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfChildListBeginScan
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: WdfChildListBeginScan
req.iface: 
req.product: Windows 10 or later.
---

# WdfChildListBeginScan function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfChildListBeginScan</b> method prepares a specified list of child devices so the driver can update the information in the list.</p>


## -syntax

````
VOID WdfChildListBeginScan(
  _In_ WDFCHILDLIST ChildList
);
````


## -parameters
<dl>

### -param <i>ChildList</i> [in]

<dd>
<p>A handle to a framework child list object.</p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A system bug check occurs if the driver supplies an invalid object handle.
</p>

## -remarks
<p>The <b>WdfChildListBeginScan</b> method marks all of the child devices in the list as missing. </p>

<p>After calling <b>WdfChildListBeginScan</b>, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545591">WdfChildListAddOrUpdateChildDescriptionAsPresent</a> repeatedly, or call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545667">WdfChildListUpdateAllChildDescriptionsAsPresent</a>, to report all of the child devices that are currently attached to the parent device. </p>

<p>After the driver has finished updating the child list, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545626">WdfChildListEndScan</a>. This call delivers the updated child list to the Plug and Play (PnP) manager. Subsequently, the framework will call the driver's <a href="https://msdn.microsoft.com/296fbe06-1680-43a8-b5c3-1a1faa19c6c3">EvtChildListCreateDevice</a> callback function for each device that the driver reported.</p>

<p>For more information about child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

<p>For a code example that uses <b>WdfChildListBeginScan</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545591">WdfChildListAddOrUpdateChildDescriptionAsPresent</a>.</p>

<p>The <b>WdfChildListBeginScan</b> method marks all of the child devices in the list as missing. </p>

<p>After calling <b>WdfChildListBeginScan</b>, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545591">WdfChildListAddOrUpdateChildDescriptionAsPresent</a> repeatedly, or call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545667">WdfChildListUpdateAllChildDescriptionsAsPresent</a>, to report all of the child devices that are currently attached to the parent device. </p>

<p>After the driver has finished updating the child list, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545626">WdfChildListEndScan</a>. This call delivers the updated child list to the Plug and Play (PnP) manager. Subsequently, the framework will call the driver's <a href="https://msdn.microsoft.com/296fbe06-1680-43a8-b5c3-1a1faa19c6c3">EvtChildListCreateDevice</a> callback function for each device that the driver reported.</p>

<p>For more information about child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

<p>For a code example that uses <b>WdfChildListBeginScan</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545591">WdfChildListAddOrUpdateChildDescriptionAsPresent</a>.</p>

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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545591">WdfChildListAddOrUpdateChildDescriptionAsPresent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545601">WdfChildListBeginIteration</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545626">WdfChildListEndScan</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545667">WdfChildListUpdateAllChildDescriptionsAsPresent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfChildListBeginScan method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
