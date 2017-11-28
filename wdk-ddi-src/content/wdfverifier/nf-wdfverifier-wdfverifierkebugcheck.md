---
UID: NF.wdfverifier.WdfVerifierKeBugCheck
title: WdfVerifierKeBugCheck
author: windows-driver-content
description: The WdfVerifierKeBugCheck function creates a bug check.
old-location: wdf\wdfverifierkebugcheck.htm
old-project: wdf
ms.assetid: 3fa8ea3d-cca0-402d-a3a8-1281ad4231d4
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfVerifierKeBugCheck
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfverifier.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfVerifierKeBugCheck
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# WdfVerifierKeBugCheck function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfVerifierKeBugCheck</b> function creates a bug check.</p>


## -syntax

````
VOID WdfVerifierKeBugCheck(
  _In_ ULONG     BugCheckCode,
  _In_ ULONG_PTR BugCheckParameter1,
  _In_ ULONG_PTR BugCheckParameter2,
  _In_ ULONG_PTR BugCheckParameter3,
  _In_ ULONG_PTR BugCheckParameter4
);
````


## -parameters
<dl>

### -param <i>BugCheckCode</i> [in]

<dd>
<p>One of the <a href="https://msdn.microsoft.com/DBA85578-97CF-4BD7-A67D-1C7AD2E9B2BB">bug check codes</a> that are defined in <i>Bugcodes.h</i>.</p>
</dd>

### -param <i>BugCheckParameter1</i> [in]

<dd>
<p>For information about this parameter, see the specified bug check code's description.</p>
</dd>

### -param <i>BugCheckParameter2</i> [in]

<dd>
<p>For information about this parameter, see the specified bug check code's description.</p>
</dd>

### -param <i>BugCheckParameter3</i> [in]

<dd>
<p>For information about this parameter, see the specified bug check code's description.</p>
</dd>

### -param <i>BugCheckParameter4</i> [in]

<dd>
<p>For information about this parameter, see the specified bug check code's description.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If your Kernel-Mode Driver Framework (KMDF) driver calls <b>WdfVerifierKeBugCheck</b>, the operating system halts and displays a <a href="https://msdn.microsoft.com/8cc42643-e231-49dd-96b0-6cb528d5d7a9">blue screen</a> unless a <a href="https://msdn.microsoft.com/e2490442-9d90-454b-95e0-db8c5d7fa19a">debugger</a> is running.</p>

<p>If your  User-Mode Driver Framework (UMDF) driver (version 2.0 or later) calls <b>WdfVerifierKeBugCheck</b>, the framework does not use  the parameters that the driver supplies.   In this case, the framework breaks into the debugger if one is connected. If a debugger is not connected, the framework generates an exception, and the default UMDF exception handler creates a minidump file. For more information about unhandled exceptions in the driver host process, see <a href="wdf.how_umdf_reports_errors">How UMDF Reports Errors</a>.</p>

<p>For more information about debugging your driver, see <a href="wdf.debugging_a_wdf_driver">Debugging WDF Drivers</a>.</p>

<p>The following code example creates a bug check that uses the <a href="https://msdn.microsoft.com/bc60b4b3-aded-4c67-bbaa-aad1b6b38d30">MULTIPLE_IRP_COMPLETE_REQUESTS</a> bug check code.</p>

<p>If your Kernel-Mode Driver Framework (KMDF) driver calls <b>WdfVerifierKeBugCheck</b>, the operating system halts and displays a <a href="https://msdn.microsoft.com/8cc42643-e231-49dd-96b0-6cb528d5d7a9">blue screen</a> unless a <a href="https://msdn.microsoft.com/e2490442-9d90-454b-95e0-db8c5d7fa19a">debugger</a> is running.</p>

<p>If your  User-Mode Driver Framework (UMDF) driver (version 2.0 or later) calls <b>WdfVerifierKeBugCheck</b>, the framework does not use  the parameters that the driver supplies.   In this case, the framework breaks into the debugger if one is connected. If a debugger is not connected, the framework generates an exception, and the default UMDF exception handler creates a minidump file. For more information about unhandled exceptions in the driver host process, see <a href="wdf.how_umdf_reports_errors">How UMDF Reports Errors</a>.</p>

<p>For more information about debugging your driver, see <a href="wdf.debugging_a_wdf_driver">Debugging WDF Drivers</a>.</p>

<p>The following code example creates a bug check that uses the <a href="https://msdn.microsoft.com/bc60b4b3-aded-4c67-bbaa-aad1b6b38d30">MULTIPLE_IRP_COMPLETE_REQUESTS</a> bug check code.</p>

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
<dt>Wdfverifier.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551164">WdfVerifierDbgBreakPoint</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfVerifierKeBugCheck function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
