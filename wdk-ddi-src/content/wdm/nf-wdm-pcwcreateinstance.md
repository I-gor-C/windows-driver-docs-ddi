---
UID: NF.wdm.PcwCreateInstance
title: PcwCreateInstance
author: windows-driver-content
description: The PcwCreateInstance function creates a new instance for the specified registered counter set.
old-location: devtest\pcwcreateinstance.htm
old-project: devtest
ms.assetid: ed9bd8fa-a6e6-465a-8415-3e9c19233419
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: PcwCreateInstance
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PcwCreateInstance
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <=APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PcwCreateInstance function



## -description
<p>The <b>PcwCreateInstance</b> function creates a new instance for the specified registered counter set.</p>


## -syntax

````
NTSTATUS PcwCreateInstance(
  _Out_ PPCW_INSTANCE     *Instance,
  _In_  PPCW_REGISTRATION Registration,
  _In_  PCUNICODE_STRING  Name,
  _In_  ULONG             Count,
  _In_  PPCW_DATA         Data
);
````


## -parameters
<dl>

### -param <i>Instance</i> [out]

<dd>
<p>A pointer to receive the newly created instance.</p>
</dd>

### -param <i>Registration</i> [in]

<dd>
<p>A pointer to the registered provider that owns this instance of the counter set.</p>
</dd>

### -param <i>Name</i> [in]

<dd>
<p>A pointer to the Unicode string that contains the name of the instance of the counter set.</p>
</dd>

### -param <i>Count</i> [in]

<dd>
<p>The number of data blocks that are associated with this instance.</p>
</dd>

### -param <i>Data</i> [in]

<dd>
<p>A pointer to an array of data blocks that contains the counter values of this instance.</p>
</dd>
</dl>

## -returns
<p>This function returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The instance was successfully created,</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_4</b></dt>
</dl><p>The number of structures, specified by <i>Count</i>, is not valid for the registered provider.</p><dl>
<dt><b>STATUS_INVALID_BUFFER_SIZE</b></dt>
</dl><p>A problem was detected with the size of the data buffer and the counter set,</p><dl>
<dt><b>STATUS_INTEGER_OVERFLOW</b></dt>
</dl><p>The size of the structure, specified by <i>Count</i>, overflows the data buffer,</p>

<p> </p>

## -remarks
<p>Before the provider uses this function, the provider must call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550323">PcwRegister</a> function to create a registration.</p>

<p>Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550316">PcwCloseInstance</a> function to close this instance.</p>

<p>Before the provider uses this function, the provider must call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550323">PcwRegister</a> function to create a registration.</p>

<p>Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550316">PcwCloseInstance</a> function to close this instance.</p>

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
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h or Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550316">PcwCloseInstance</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550323">PcwRegister</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [devtest\devtest]:%20PcwCreateInstance function%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
