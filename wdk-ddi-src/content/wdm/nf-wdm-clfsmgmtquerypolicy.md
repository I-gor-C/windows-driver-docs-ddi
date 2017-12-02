---
UID: NF.wdm.ClfsMgmtQueryPolicy
title: ClfsMgmtQueryPolicy
author: windows-driver-content
description: The ClfsMgmtQueryPolicy routine retrieves a specific CLFS_MGMT_POLICY structure for a log.
old-location: kernel\clfsmgmtquerypolicy.htm
old-project: kernel
ms.assetid: c9cc9124-ee15-40df-b149-a9f3b26d7c24
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ClfsMgmtQueryPolicy
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ClfsMgmtQueryPolicy
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

# ClfsMgmtQueryPolicy function



## -description
<p>The <b>ClfsMgmtQueryPolicy</b> routine retrieves a specific <a href="..\wdm\ns-wdm--clfs-mgmt-policy.md">CLFS_MGMT_POLICY</a> structure for a log.</p>


## -syntax

````
NTSTATUS ClfsMgmtQueryPolicy(
  _In_  PLOG_FILE_OBJECT      LogFile,
  _In_  CLFS_MGMT_POLICY_TYPE PolicyType,
  _Out_ PCLFS_MGMT_POLICY     Policy,
  _Out_ PULONG                PolicyLength
);
````


## -parameters
<dl>

### -param LogFile [in]

<dd>
<p>A pointer to a <a href="kernel.log_file_object">LOG_FILE_OBJECT</a> structure that represents the CLFS log whose policy is being retrieved.</p>
</dd>

### -param PolicyType [in]

<dd>
<p>A value of the <a href="..\wdm\ne-wdm--clfs-mgmt-policy-type.md">CLFS_MGMT_POLICY_TYPE</a> enumeration that identifies the type of policy to be retrieved.</p>
</dd>

### -param Policy [out]

<dd>
<p>An instance of the <a href="..\wdm\ns-wdm--clfs-mgmt-policy.md">CLFS_MGMT_POLICY</a> structure that contains the policy.</p>
</dd>

### -param PolicyLength [out]

<dd>
<p>The length of the <i>Policy</i> parameter.</p>
</dd>
</dl>

## -returns
<p>The <b>ClfsMgmtQueryPolicy</b> routine returns one of the following NTSTATUS values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>CLFS management has retrieved the requested policy.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>CLFS management was not able to process the request.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The value of the <i>PolicyType</i> parameter is not valid for the <b>CLFS_MGMT_POLICY_TYPE</b> enumeration.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_1</b></dt>
</dl><p>A <b>NULL</b> value was supplied for the <i>LogFile</i> parameter.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl><p>The value of the <i>PolicyLength</i> parameter is less than the size of an instance of the <b>CLFS_MGMT_POLICY</b> structure.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There is insufficient memory to complete the operation.</p><dl>
<dt><b>STATUS_LOG_POLICY_NOT_INSTALLED</b></dt>
</dl><p>No policy of this type has been registered for the log file.</p>

<p> </p>

<p>This routine might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS Values</a>.</p>

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
<p>Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.</p>
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
<a href="..\wdm\ns-wdm--clfs-mgmt-policy.md">CLFS_MGMT_POLICY</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--clfs-mgmt-policy-type.md">CLFS_MGMT_POLICY_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ClfsMgmtQueryPolicy routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
