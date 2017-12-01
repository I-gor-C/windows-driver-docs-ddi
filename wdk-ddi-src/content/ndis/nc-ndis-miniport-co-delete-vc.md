---
UID: NC.ndis.MINIPORT_CO_DELETE_VC
title: MINIPORT_CO_DELETE_VC
author: windows-driver-content
description: The MiniportCoDeleteVc function is required for connection-oriented miniports.
old-location: netvista\miniportcodeletevc.htm
old-project: netvista
ms.assetid: ed9b6ad1-059b-47d9-b1f7-10d498c5d2d4
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    MiniportCoDeleteVc (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    MiniportCoDeleteVc (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MiniportCoDeleteVc
req.alt-loc: Ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# MINIPORT_CO_DELETE_VC callback



## -description
<p>The 
  <i>MiniportCoDeleteVc</i> function is required for connection-oriented miniports. 
  <i>MiniportCoDeleteVc</i> indicates that a VC is being torn down and deleted by NDIS.</p>


## -prototype

````
MINIPORT_CO_DELETE_VC MiniportCoDeleteVc;

NDIS_STATUS MiniportCoDeleteVc(
  _In_ NDIS_HANDLE MiniportVcContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>MiniportVcContext</i> [in]

<dd>
<p>Specifies the handle to a miniport driver-allocated context area in which the miniport driver
     maintains its per-VC state. The miniport driver supplied this handle to NDIS from its 
     <a href="..\ndis\nc-ndis-miniport-co-create-vc.md">MiniportCoCreateVc</a> function.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the miniport driver successfully freed all resources allocated for this
       VC.</p>

<p> </p>

## -remarks
<p><i>MiniportCoDeleteVcmust</i> be written as a synchronous function and cannot, under any circumstances,
    return NDIS_STATUS_PENDING without causing a system-wide failure.</p>

<p><i>MiniportCoDeleteVc</i> frees any resources allocated on a per-VC basis and stored in the context area 
    <i>MiniportVcContext</i> . The miniport driver must also free the 
    <i>MiniportVcContext</i> that is allocated in its 
    <i>MiniportCoCreateVc</i> function.</p>

<p>To define a <i>MiniportCoDeleteVc</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportCoDeleteVc</i> function that is named "MyCoDeleteVc", use the <b>MINIPORT_CO_DELETE_VC</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_CO_DELETE_VC</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_CO_DELETE_VC</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/9e682407-3500-4ac6-9a9f-e25224340403">MiniportCoDeleteVc (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <i>MiniportCoDeleteVc (NDIS
   5.1)</i>) in Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-co-create-vc.md">MiniportCoCreateVc</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_CO_DELETE_VC callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
