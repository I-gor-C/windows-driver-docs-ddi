---
UID: NF.wdm.ClfsMgmtSetLogFileSizeAsClient
title: ClfsMgmtSetLogFileSizeAsClient
author: windows-driver-content
description: The ClfsMgmtSetLogFileSizeAsClient routine sets the log file size by adding containers to a client log or deleting containers from a client log.
old-location: kernel\clfsmgmtsetlogfilesizeasclient_.htm
old-project: kernel
ms.assetid: C049A6BE-6E2B-46F2-B7CF-316E4CDB35E4
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ClfsMgmtSetLogFileSizeAsClient
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ClfsMgmtSetLogFileSizeAsClient
req.alt-loc: Clfs.sys,Ext-MS-Win-fs-clfs-l1-1-0.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: Clfs.sys
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# ClfsMgmtSetLogFileSizeAsClient function



## -description
<p>The <b>ClfsMgmtSetLogFileSizeAsClient</b>  routine sets the log file size by adding containers to a client log or deleting containers from a client log.</p>


## -syntax

````
NTSTATUS ClfsMgmtSetLogFileSizeAsClient (
  _In_      PLOG_FILE_OBJECT                     LogFile,
  _In_opt_  PCLFS_MGMT_CLIENT                    ClientCookie,
  _In_      PULONGLONG                           NewSizeInContainers,
  _Out_opt_ PULONGLONG                           ResultingSizeInContainers,
  _In_opt_  PCLFS_SET_LOG_SIZE_COMPLETE_CALLBACK CompletionRoutine,
  _In_opt_  PVOID                                CompletionRoutineData
);
````


## -parameters
<dl>

### -param LogFile [in]

<dd>
<p>A pointer to a <a href="kernel.log_file_object">LOG_FILE_OBJECT</a> structure that represents the Common Log File System (CLFS) log, or a stream within the log, to which containers are being added or deleted. The value of this parameter is obtained through a call to the <a href="..\wdm\nf-wdm-clfscreatelogfile.md">ClfsCreateLogFile</a> routine.</p>
</dd>

### -param ClientCookie [in, optional]

<dd>
<p>A pointer to a client-supplied cookie. The value of this parameter should be the <b>CLFS_MGMT_CLIENT</b> structure that is obtained through a call to the <a href="..\wdm\nf-wdm-clfsmgmtregistermanagedclient.md">ClfsMgmtRegisterManagedClient</a> routine.</p>
</dd>

### -param NewSizeInContainers [in]

<dd>
<p>The desired size of the log, expressed in the number of containers. There can be at most 1,024 containers for a log file.</p>
</dd>

### -param ResultingSizeInContainers [out, optional]

<dd>
<p>The actual size of the log, expressed in the number of containers.</p>
</dd>

### -param CompletionRoutine [in, optional]

<dd>
<p> Not used.</p>
</dd>

### -param CompletionRoutineData [in, optional]

<dd>
<p> Not used. </p>
</dd>
</dl>

## -returns
<p>The <b>ClfsMgmtSetLogFileSizeAsClient</b> routine returns an NTSTATUS value.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The log file size has been set. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER_1</b></dt>
</dl><p>The value of the <i>LogFile</i> parameter is <b>NULL</b>, or the contents of the <i>NewSizeInContainers</i> parameter is 1.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl><p>The value of the <i>NewSizeInContainers</i> parameter is <b>NULL</b>.</p><dl>
<dt><b>STATUS_LOG_POLICY_INVALID</b></dt>
</dl><p>The installed set of policies on the log is invalid. This might be due to an invalid <a href="fs.clfsmgmtpolicyautoshrink">ClfsMgmtPolicyAutoShrink</a> policy or <a href="fs.clfsmgmtpolicymaximumsize">ClfsMgmtPolicyMaximumSize</a> policy.</p><dl>
<dt><b>STATUS_COULD_NOT_RESIZE_LOG</b></dt>
</dl><p>CLFS management could not delete enough containers to reach the value in <i>NewSizeInContainers</i>.</p><dl>
<dt><b>STATUS_LOG_POLICY_CONFLICT</b></dt>
</dl><p>A policy on the specified log   prevented the operation from completing. This may occur if CLFS management could not add enough containers to the log to reach the value in <i>NewSizeInContainers</i>. This might be due to a conflict with a policy that the client set.</p>

<p> </p>

<p>This routine might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Clfs.sys</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.clfs_management_library_routines">CLFS Management Library Routines</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ClfsMgmtSetLogFileSizeAsClient  routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
