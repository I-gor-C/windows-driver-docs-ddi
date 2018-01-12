---
UID: NF:wdfchildlist.WdfChildListBeginScan
title: WdfChildListBeginScan function
author: windows-driver-content
description: The WdfChildListBeginScan method prepares a specified list of child devices so the driver can update the information in the list.
old-location: wdf\wdfchildlistbeginscan.htm
old-project: wdf
ms.assetid: 08951cde-d9d2-4de6-bb63-7c3e7cf1f92f
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: WdfChildListBeginScan
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
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
req.typenames: WDF_RETRIEVE_CHILD_FLAGS
req.product: Windows 10 or later.
---

# WdfChildListBeginScan function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfChildListBeginScan</b> method prepares a specified list of child devices so the driver can update the information in the list.



## -syntax

````
VOID WdfChildListBeginScan(
  _In_ WDFCHILDLIST ChildList
);
````


## -parameters

### -param ChildList [in]

A handle to a framework child list object.


## -returns
None.

A system bug check occurs if the driver supplies an invalid object handle.



## -remarks
The <b>WdfChildListBeginScan</b> method marks all of the child devices in the list as missing. 

After calling <b>WdfChildListBeginScan</b>, the driver can call <a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent.md">WdfChildListAddOrUpdateChildDescriptionAsPresent</a> repeatedly, or call <a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistupdateallchilddescriptionsaspresent.md">WdfChildListUpdateAllChildDescriptionsAsPresent</a>, to report all of the child devices that are currently attached to the parent device. 

After the driver has finished updating the child list, it must call <a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistendscan.md">WdfChildListEndScan</a>. This call delivers the updated child list to the Plug and Play (PnP) manager. Subsequently, the framework will call the driver's <a href="..\wdfchildlist\nc-wdfchildlist-evt_wdf_child_list_create_device.md">EvtChildListCreateDevice</a> callback function for each device that the driver reported.

For more information about child lists, see <a href="https://msdn.microsoft.com/6e46b456-7d2d-4c6e-8692-7f310366387d">Dynamic Enumeration</a>.

For a code example that uses <b>WdfChildListBeginScan</b>, see <a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent.md">WdfChildListAddOrUpdateChildDescriptionAsPresent</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfchildlist.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="https://msdn.microsoft.com/51db6f3c-45cb-46a7-9dd4-2bab67893fea">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent.md">WdfChildListAddOrUpdateChildDescriptionAsPresent</a>
</dt>
<dt>
<a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistbeginiteration.md">WdfChildListBeginIteration</a>
</dt>
<dt>
<a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistendscan.md">WdfChildListEndScan</a>
</dt>
<dt>
<a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistupdateallchilddescriptionsaspresent.md">WdfChildListUpdateAllChildDescriptionsAsPresent</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfChildListBeginScan method%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

