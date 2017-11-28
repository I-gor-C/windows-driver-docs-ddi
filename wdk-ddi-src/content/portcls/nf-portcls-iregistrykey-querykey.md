---
UID: NF.portcls.IRegistryKey.QueryKey
title: IRegistryKey::QueryKey
author: windows-driver-content
description: The QueryKey method retrieves information about a registry key, including the key name, key class, and the number of subkeys and their sizes.
old-location: audio\iregistrykey_querykey.htm
old-project: audio
ms.assetid: 1b2642da-1b04-49a8-942e-6eb93afd12f2
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IRegistryKey, QueryKey, IRegistryKey::QueryKey
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRegistryKey.QueryKey
req.alt-loc: portcls.h
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
req.iface: IRegistryKey
---

# IRegistryKey::QueryKey method



## -description
<p>The <code>QueryKey</code> method retrieves information about a registry key, including the key name, key class, and the number of subkeys and their sizes.</p>


## -syntax

````
NTSTATUS QueryKey(
  [in]  KEY_INFORMATION_CLASS KeyInformationClass,
  [out] PVOID                 KeyInformation,
  [in]  ULONG                 Length,
  [out] PULONG                ResultLength
);
````


## -parameters
<dl>

### -param <i>KeyInformationClass</i> [in]

<dd>
<p>Specifies the type of information to be returned in the buffer. Set this parameter to one of the following KEY_INFORMATION_CLASS enumeration values:</p>
<ul>
<li>
<p><b>KeyBasicInformation</b></p>
</li>
<li>
<p><b>KeyFullInformation</b></p>
</li>
<li>
<p><b>KeyNodeInformation</b></p>
</li>
</ul>
</dd>

### -param <i>KeyInformation</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer into which the method writes the requested data. The buffer holds a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff553355">KEY_BASIC_INFORMATION</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff553367">KEY_FULL_INFORMATION</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff553392">KEY_NODE_INFORMATION</a>, depending on the value of <i>KeyInformationClass</i>. The structure is followed by a string of Unicode characters whose size depends on the type of information being requested about the key and the length of the key's name or class string.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Size in bytes of the <i>KeyInformation</i> buffer, which the caller must set according to the given <i>KeyInformationClass</i>. To receive all the requested data, the buffer must be at least as large as the size of the requested data.</p>
</dd>

### -param <i>ResultLength</i> [out]

<dd>
<p>Output pointer for the length of the resulting data. This parameter points to a caller-allocated ULONG variable into which the method writes a count specifying the number of bytes actually written into the <i>KeyInformation</i> buffer. If the specified buffer length is too small to contain the information, however, the method instead outputs the required buffer size and returns STATUS_BUFFER_OVERFLOW or STATUS_BUFFER_TOO_SMALL. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p><code>QueryKey</code> returns STATUS_SUCCESS if the call was successful in copying the requested information to the <i>KeyInformation</i> buffer. If the specified buffer size is too small to receive all of the requested information, the method returns STATUS_BUFFER_OVERFLOW. If the specified buffer size is too small to receive any of the requested information, the method returns STATUS_BUFFER_TOO_SMALL. Otherwise, the method returns an appropriate error status code. The following table shows some of the possible error codes.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Indicates that one of the parameters passed to the method is not valid.</p>

<p> </p>

## -remarks
<p>If the <i>KeyInformation</i> buffer is too small to hold the requested information, the method writes the required size to *<i>ResultLength</i> and returns a status code of either STATUS_BUFFER_OVERFLOW or STATUS_BUFFER_TOO_SMALL. The method returns STATUS_BUFFER_OVERFLOW if it succeeded in writing only part of the requested information to the buffer. The method returns STATUS_BUFFER_TOO_SMALL if it was unable to write any information to the buffer. The value written to *<i>ResultLength</i> indicates the minimum buffer size required to hold all the requested information.</p>

<p>If the <i>KeyInformation</i> buffer is too small to hold the requested information, the method writes the required size to *<i>ResultLength</i> and returns a status code of either STATUS_BUFFER_OVERFLOW or STATUS_BUFFER_TOO_SMALL. The method returns STATUS_BUFFER_OVERFLOW if it succeeded in writing only part of the requested information to the buffer. The method returns STATUS_BUFFER_TOO_SMALL if it was unable to write any information to the buffer. The value written to *<i>ResultLength</i> indicates the minimum buffer size required to hold all the requested information.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536965">IRegistryKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553355">KEY_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553367">KEY_FULL_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553392">KEY_NODE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567060">ZwQueryKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IRegistryKey::QueryKey method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
