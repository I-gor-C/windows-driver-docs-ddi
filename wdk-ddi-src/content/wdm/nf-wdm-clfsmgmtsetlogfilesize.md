---
UID: NF.wdm.ClfsMgmtSetLogFileSize
title: ClfsMgmtSetLogFileSize
author: windows-driver-content
description: The ClfsMgmtSetLogFileSize routine adds containers to a log or deletes containers from a log.
old-location: kernel\clfsmgmtsetlogfilesize.htm
old-project: kernel
ms.assetid: 76588bdd-ceb8-4c8b-bcd7-23184feacf86
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ClfsMgmtSetLogFileSize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows Server 2003 R2 and Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ClfsMgmtSetLogFileSize
req.alt-loc: Clfs.sys,Ext-MS-Win-fs-clfs-l1-1-0.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Clfs.lib
req.dll: Clfs.sys
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ClfsMgmtSetLogFileSize function



## -description
<p>The <b>ClfsMgmtSetLogFileSize</b> routine adds containers to a log or deletes containers from a log.</p>


## -syntax

````
NTSTATUS ClfsMgmtSetLogFileSize(
  _In_     PLOG_FILE_OBJECT                     LogFile,
  _In_     PULONGLONG                           NewSizeInContainers,
  _Out_    PULONGLONG                           ResultingSizeInContainers,
  _In_opt_ PCLFS_SET_LOG_SIZE_COMPLETE_CALLBACK CompletionRoutine,
  _In_opt_ PVOID                                CompletionRoutineData
);
````


## -parameters
<dl>

### -param LogFile [in]

<dd>
<p>A pointer to a <a href="kernel.log_file_object">LOG_FILE_OBJECT</a> structure that represents the CLFS log, or a stream within the log, to which containers are being added or deleted.</p>
</dd>

### -param NewSizeInContainers [in]

<dd>
<p>A pointer to the requested log size. The caller sets this parameter to one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>0</td>
<td>
<p>Enforce the minimum size policy. For more information about this policy, see <a href="..\wdm\nf-wdm-clfsmgmtinstallpolicy.md">ClfsMgmtInstallPolicy</a>.</p>
<p>If a minimum size policy is not installed, one of the following occurs:</p>
<ul>
<li>If the log currently has less than 2 containers, the log will be expanded to a size of 2 containers.</li>
<li>If the log currently has 2 or more containers, no changes are made and the call succeeds.</li>
</ul>
<p>If a minimum size policy is installed, one of the following occurs:</p>
<ul>
<li>If the log currently has less than the minimum number of containers specified by the minimum size policy, the log expands to the policy-specified minimum number of containers.</li>
<li>If the number of containers in the log is greater than or equal to the minimum number of containers specified by the minimum size policy, no changes are made and the call succeeds with no error.</li>
</ul>
</td>
</tr>
<tr>
<td>1</td>
<td>Invalid value. The call fails and returns STATUS_INVALID_VALUE.</td>
</tr>
<tr>
<td>2 to 1023</td>
<td>
<p>The desired size of the log, expressed as the number of containers.</p>
<p>If this number is smaller than the minimum number of containers specified by the installed policy, the call fails with ERROR_COULD_NOT_RESIZE_LOG.</p>
<p>If this number is larger than the maximum number of containers specified by the installed policy, the log expands only as far as the policy-specified maximum number of containers, and the call succeeds with no error.</p>
</td>
</tr>
<tr>
<td>1024 to MAXULONGLONG</td>
<td>
<p>If no maximum size policy is installed, the call fails and returns ERROR_LOG_POLICY_CONFLICT.</p>
<p>If a maximum size policy is installed, the log expands to the maximum number of containers specified by the maximum size policy and the call succeeds with no error.</p>
</td>
</tr>
</table>
<p> </p>
<p>To determine the actual log size, which might be different from the requested size, use the <i>ResultingSizeInContainers</i> parameter.</p>
</dd>

### -param ResultingSizeInContainers [out]

<dd>
<p>A pointer to the resulting log size. If successful, the routine writes the actual size of the log, expressed as the number of containers in the log, to the location pointed to by this parameter.</p>
</dd>

### -param CompletionRoutine [in, optional]

<dd>
<p> Not used.  Set to NULL.</p>
</dd>

### -param CompletionRoutineData [in, optional]

<dd>
<p> Not used. Set to NULL.</p>
</dd>
</dl>

## -returns
<p>The <b>ClfsMgmtSetLogFileSize</b> routine returns one of the following NTSTATUS values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The log file size has been set. The <i>ResultingSizeInContainers</i> parameter contains the current size of the log.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>CLFS management was not able to set the log file size.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_1</b></dt>
</dl><p>The value of the <i>LogFile</i> parameter is <b>NULL</b>, or the contents of the <i>NewSizeInContainers</i> parameter is 1.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl><p>The value of the <i>NewSizeInContainers</i> parameter is <b>NULL</b>.</p><dl>
<dt><b>STATUS_LOG_POLICY_INVALID</b></dt>
</dl><p>There is a conflict between the maximum size and minimum size policies for the log.</p><dl>
<dt><b>STATUS_COULD_NOT_RESIZE_LOG</b></dt>
</dl><p>CLFS management could not delete enough containers to reach <i>NewSizeInContainers</i>.</p><dl>
<dt><b>STATUS_LOG_POLICY_CONFLICT</b></dt>
</dl><p>CLFS management could not add enough containers to the log to reach <i>NewSizeInContainers</i>. This might be due to a conflict with a policy that the client set.</p>

<p> </p>

<p>This routine might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS Values</a>.</p>

## -remarks
<p>The <b>ClfsMgmtSetLogFileSize</b> routine is typically used only when a client starts or stops. Do not call the <b>ClfsMgmtSetLogFileSize</b> routine from within your <a href="kernel.clfsadvancetailcallback">ClfsAdvanceTailCallback</a> function.</p>

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
<p>Available starting with Windows Server 2003 R2 and Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Clfs.lib</dt>
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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-clfsmgmtinstallpolicy.md">ClfsMgmtInstallPolicy</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--clfs-mgmt-policy-type.md">CLFS_MGMT_POLICY_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ClfsMgmtSetLogFileSize routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
