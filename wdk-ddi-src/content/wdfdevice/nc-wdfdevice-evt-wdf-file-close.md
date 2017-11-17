---
UID: NC.wdfdevice.EVT_WDF_FILE_CLOSE
title: EVT_WDF_FILE_CLOSE
author: windows-driver-content
description: A driver's EvtFileClose callback function handles operations that must be performed when all of an application's accesses to a device have been closed.
old-location: wdf\evtfileclose.htm
ms.assetid: 8ddcb9cb-d184-4ec8-a321-599394a8512e
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: EvtFileClose
req.alt-loc: Wdfdevice.h
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
ms.keywords: WDF_REL_TIMEOUT_IN_US
req.iface: 
req.product: Windows 10 or later.
---

# EVT_WDF_FILE_CLOSE callback



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>A driver's <i>EvtFileClose</i> callback function handles operations that must be performed when all of an application's accesses to a device have been closed.</p>


## -prototype

````
EVT_WDF_FILE_CLOSE EvtFileClose;

VOID EvtFileClose(
  _In_ WDFFILEOBJECT FileObject
)
{ ... }
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>A handle to a framework file object, which was previously received by the driver's <a href="https://msdn.microsoft.com/ee44c0bf-1fca-442d-8871-df6079e89ced">EvtDeviceFileCreate</a> callback function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The framework calls a driver's <i>EvtFileClose</i> callback function when the last handle for a file object has been closed and released, and all outstanding I/O requests have been completed or canceled.</p>

<p>The device might not be in its working (D0) state.</p>

<p>Before the framework calls a driver's <i>EvtFileClose</i> callback function, it calls the driver's <a href="https://msdn.microsoft.com/8ce3d316-3976-4af5-a0ae-af4e93f380a1">EvtFileCleanup</a> callback function.</p>

<p>The <i>EvtFileClose</i> callback function is called synchronously, in an arbitrary thread context. </p>

<p>To register an <i>EvtFileClose</i> callback function, the driver must call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546107">WdfDeviceInitSetFileObjectConfig</a> method.</p>

<p>For more information about framework file objects and the <i>EvtFileClose</i> callback function, see <a href="wdf.framework_file_objects">Framework File Objects</a>.</p>

<p>To define an <i>EvtFileClose</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtFileClose</i> callback function that is named <i>MyFileClose</i>, use the <b>EVT_WDF_FILE_CLOSE</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_FILE_CLOSE</b> function type is defined in the Wdfdevice.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_FILE_CLOSE</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

<p>The framework calls a driver's <i>EvtFileClose</i> callback function when the last handle for a file object has been closed and released, and all outstanding I/O requests have been completed or canceled.</p>

<p>The device might not be in its working (D0) state.</p>

<p>Before the framework calls a driver's <i>EvtFileClose</i> callback function, it calls the driver's <a href="https://msdn.microsoft.com/8ce3d316-3976-4af5-a0ae-af4e93f380a1">EvtFileCleanup</a> callback function.</p>

<p>The <i>EvtFileClose</i> callback function is called synchronously, in an arbitrary thread context. </p>

<p>To register an <i>EvtFileClose</i> callback function, the driver must call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546107">WdfDeviceInitSetFileObjectConfig</a> method.</p>

<p>For more information about framework file objects and the <i>EvtFileClose</i> callback function, see <a href="wdf.framework_file_objects">Framework File Objects</a>.</p>

<p>To define an <i>EvtFileClose</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtFileClose</i> callback function that is named <i>MyFileClose</i>, use the <b>EVT_WDF_FILE_CLOSE</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_FILE_CLOSE</b> function type is defined in the Wdfdevice.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_FILE_CLOSE</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551319">WDF_FILEOBJECT_CONFIG</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_FILE_CLOSE callback function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
