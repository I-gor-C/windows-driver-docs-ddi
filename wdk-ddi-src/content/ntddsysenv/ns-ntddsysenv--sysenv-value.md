---
UID: NS.ntddsysenv._SYSENV_VALUE
title: SYSENV_VALUE
author: windows-driver-content
description: Stores the value of a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_GET_VARIABLE request.
old-location: kernel\sysenv_value.htm
old-project: kernel
ms.assetid: 4F79D820-29D4-4D38-A09C-8A5E968C1479
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: SYSENV_VALUE, SYSENV_VALUE, *PSYSENV_VALUE
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
req.alt-api: SYSENV_VALUE
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

# SYSENV_VALUE structure



## -description
<p>Stores the value of a system environment variable using
    SysEnv device. This structure is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/mt791526">IOCTL_SYSENV_GET_VARIABLE</a> request.</p>


## -syntax

````
typedef struct _SYSENV_VALUE {
  ULONG     Attributes;
  ULONG     ValueLength;
  ValueData UCHAR[ANYSIZE_ARRAY];
} SYSENV_VALUE, *PSYSENV_VALUE;
````


## -struct-fields
<dl>

### -field Attributes

<dd>
<p>Attributes of the system environment variable.</p>
</dd>

### -field ValueLength

<dd>
<p>The length of the value of the system environment variable.</p>
</dd>

### -field UCHAR

<dd>
<p>The value of the system environment variable.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt791526">IOCTL_SYSENV_GET_VARIABLE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20SYSENV_VALUE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
