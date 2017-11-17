---
UID: NF.ntddk.PshedSynchronizeExecution
title: PshedSynchronizeExecution
author: windows-driver-content
description: The PshedSynchronizeExecution function synchronizes the execution of a given function with the hardware error processing for an error source.
old-location: whea\pshedsynchronizeexecution.htm
ms.assetid: 299fd2fc-d7f4-4176-addd-d45d010b1056
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: whea
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PshedSynchronizeExecution
req.alt-loc: Pshed.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Pshed.lib
req.dll: Pshed.dll
req.irql: <= DIRQL
ms.keywords: PshedSynchronizeExecution
req.iface: 
---

# PshedSynchronizeExecution function



## -description
<p>The <b>PshedSynchronizeExecution</b> function synchronizes the execution of a given function with the hardware error processing for an error source.</p>


## -syntax

````
BOOLEAN PshedSynchronizeExecution(
  _In_ PWHEA_ERROR_SOURCE_DESCRIPTOR ErrorSource,
  _In_ PKSYNCHRONIZE_ROUTINE         SynchronizeRoutine,
  _In_ PVOID                         SynchronizeContext
);
````


## -parameters
<dl>

### -param <i>ErrorSource</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure that describes an error source.</p>
</dd>

### -param <i>SynchronizeRoutine</i> [in]

<dd>
<p>A pointer to a caller-supplied function whose execution is synchronized with the hardware error processing for the error source described by the <i>ErrorSource</i> parameter. A <i>SynchronizeRoutine</i> function is declared as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>BOOLEAN
SynchronizeRoutine(
    _In_ PVOID  SynchronizeContext
    );</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -param <a id="SynchronizeContext"></a><a id="synchronizecontext"></a><a id="SYNCHRONIZECONTEXT"></a><i>SynchronizeContext</i>

<dd>
<p>The context value that is passed in the <i>SynchronizeContext</i> parameter to the <b>PshedSynchronizeExecution</b> function.</p>
</dd>
</dl>
</dd>

### -param <i>SynchronizeContext</i> [in]

<dd>
<p>A pointer to a caller-supplied context area that is passed to the function pointed to by the <i>SynchronizeRoutine</i> parameter.</p>
</dd>
</dl>

## -returns
<p><b>PshedSynchronizeExecution</b> returns the value that is returned by the function pointed to by the <i>SynchronizeRoutine</i> parameter.</p>

## -remarks
<p>A PSHED plug-in calls the <b>PshedSynchronizeExecution</b> function to synchronize the execution of a given function with the hardware error processing for an error source. This is required whenever a PSHED plug-in shares resources between code that executes outside of the normal hardware error processing flow and code that executes as part of the normal hardware error processing flow. For more information about the processing of hardware errors, see <a href="NULL">Error Processing</a>.</p>

<p>When this function is called, the following occurs:</p>

<p>The IRQL is raised to the IRQL at which the low-level hardware error handler (LLHEH) for the error source executes.</p>

<p>Access to the context area specified by the <i>SynchronizeContext</i> parameter is synchronized with the LLHEH by acquiring the associated spin lock.</p>

<p>The function specified in the <i>SynchronizeRoutine</i> parameter is called.</p>

<p>Callers of the <b>PshedSynchronizeExecution</b> function must be running at IRQL &lt;= DIRQL, that is, less than or equal to the IRQL at which the LLHEH for the error source executes.</p>

<p>A PSHED plug-in calls the <b>PshedSynchronizeExecution</b> function to synchronize the execution of a given function with the hardware error processing for an error source. This is required whenever a PSHED plug-in shares resources between code that executes outside of the normal hardware error processing flow and code that executes as part of the normal hardware error processing flow. For more information about the processing of hardware errors, see <a href="NULL">Error Processing</a>.</p>

<p>When this function is called, the following occurs:</p>

<p>The IRQL is raised to the IRQL at which the low-level hardware error handler (LLHEH) for the error source executes.</p>

<p>Access to the context area specified by the <i>SynchronizeContext</i> parameter is synchronized with the LLHEH by acquiring the associated spin lock.</p>

<p>The function specified in the <i>SynchronizeRoutine</i> parameter is called.</p>

<p>Callers of the <b>PshedSynchronizeExecution</b> function must be running at IRQL &lt;= DIRQL, that is, less than or equal to the IRQL at which the LLHEH for the error source executes.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Pshed.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Pshed.dll</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DIRQL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20PshedSynchronizeExecution function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
