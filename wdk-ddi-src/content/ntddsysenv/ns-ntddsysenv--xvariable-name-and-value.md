---
UID: NS.ntddsysenv._XVARIABLE_NAME_AND_VALUE
title: XVARIABLE_NAME_AND_VALUE
author: windows-driver-content
description: Stores the name and value of a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_ENUM_VARIABLES and IOCTL_SYSENV_SET_VARIABLE requests.
old-location: kernel\xvariable_name_and_value.htm
old-project: kernel
ms.assetid: 46E892A7-2813-4C50-BE91-B5267696E2A5
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: XVARIABLE_NAME_AND_VALUE, XVARIABLE_NAME_AND_VALUE, *PXVARIABLE_NAME_AND_VALUE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddsysenv.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: XVARIABLE_NAME_AND_VALUE
req.alt-loc: Ntddsysenv.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# XVARIABLE_NAME_AND_VALUE structure



## -description
<p>Stores the name and value of a system environment variable using
    SysEnv device. This structure is used in the <a href="..\ntddsysenv\ni-ntddsysenv-ioctl-sysenv-enum-variables.md">IOCTL_SYSENV_ENUM_VARIABLES</a> and <a href="..\ntddsysenv\ni-ntddsysenv-ioctl-sysenv-set-variable.md">IOCTL_SYSENV_SET_VARIABLE</a> requests.</p>


## -syntax

````
typedef struct _XVARIABLE_NAME_AND_VALUE {
  ULONG 				NextEntryOffset;
  ULONG ValueOffset;
  ULONG ValueLength;
  ULONG Attributes;
  GUID  VendorGuid;
  WCHAR Name[ANYSIZE_ARRAY];
} XVARIABLE_NAME_AND_VALUE, *PXVARIABLE_NAME_AND_VALUE;
````


## -struct-fields
<dl>

### -field <b>				NextEntryOffset</b>

<dd>
<p>The location of the next entry in the array of XVARIABLE_NAME structures reprieved by the  <a href="..\ntddsysenv\ni-ntddsysenv-ioctl-sysenv-enum-variables.md">IOCTL_SYSENV_ENUM_VARIABLES</a> request.</p>
</dd>

### -field <b>ValueOffset</b>

<dd>
<p>The value of the system environment variable.</p>
</dd>

### -field <b>ValueLength</b>

<dd>
<p>The length of the value.</p>
</dd>

### -field <b>Attributes</b>

<dd>
<p>Attributes of the system environment variable.</p>
</dd>

### -field <b>VendorGuid</b>

<dd>
<p>The vendor GUID.</p>
</dd>

### -field <b>Name</b>

<dd>
<p>Name of the system environment variable.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddsysenv.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddsysenv\ni-ntddsysenv-ioctl-sysenv-enum-variables.md">IOCTL_SYSENV_ENUM_VARIABLES</a>
</dt>
<dt>
<a href="..\ntddsysenv\ni-ntddsysenv-ioctl-sysenv-set-variable.md">IOCTL_SYSENV_SET_VARIABLE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20XVARIABLE_NAME_AND_VALUE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
