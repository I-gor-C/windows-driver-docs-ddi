---
UID: NF.wdm.ClfsMgmtRemovePolicy
title: ClfsMgmtRemovePolicy function
author: windows-driver-content
description: The ClfsMgmtRemovePolicy routine resets a log's CLFS_MGMT_POLICY structure to its default value.
old-location: kernel\clfsmgmtremovepolicy.htm
old-project: kernel
ms.assetid: 6f0ae6fc-4f2f-4a1a-ac2f-93689f6b7d50
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: ClfsMgmtRemovePolicy
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
req.alt-api: ClfsMgmtRemovePolicy
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
req.product: Windows 10 or later.
---

# ClfsMgmtRemovePolicy function



## -description
The <b>ClfsMgmtRemovePolicy</b> routine resets a log's <a href="kernel.clfs_mgmt_policy">CLFS_MGMT_POLICY</a> structure to its default value.



## -syntax

````
NTSTATUS ClfsMgmtRemovePolicy(
  _In_ PLOG_FILE_OBJECT      LogFile,
  _In_ CLFS_MGMT_POLICY_TYPE PolicyType
);
````


## -parameters

### -param LogFile [in]

A pointer to a <a href="kernel.log_file_object">LOG_FILE_OBJECT</a> structure that represents the CLFS log whose policy is being removed.


### -param PolicyType [in]

A value of the <a href="kernel.clfs_mgmt_policy_type">CLFS_MGMT_POLICY_TYPE</a> enumeration that supplies the type of the policy to be removed.


## -returns
The <b>ClfsMgmtRemovePolicy</b> routine returns one of the following NTSTATUS values:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>CLFS management has removed the requested policy.
<dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl>CLFS management was not able to process the request.
<dl>
<dt><b>STATUS_INVALID_PARAMETER_1</b></dt>
</dl>A <b>NULL</b> value was supplied for the <i>LogFile</i> parameter.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>There is insufficient memory to complete the operation.
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>The value of the <i>PolicyType</i> parameter is not a valid value for the <b>CLFS_MGMT_POLICY_TYPE</b> enumeration.
<dl>
<dt><b>STATUS_LOG_POLICY_NOT_INSTALLED</b></dt>
</dl>No policy of this type has been registered for the log file.

 

This routine might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS Values</a>.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Clfs.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Clfs.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= APC_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.clfs_mgmt_policy">CLFS_MGMT_POLICY</a>
</dt>
<dt>
<a href="kernel.clfs_mgmt_policy_type">CLFS_MGMT_POLICY_TYPE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ClfsMgmtRemovePolicy routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

