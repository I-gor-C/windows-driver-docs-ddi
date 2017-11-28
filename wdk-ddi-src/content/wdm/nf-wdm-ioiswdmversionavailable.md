---
UID: NF.wdm.IoIsWdmVersionAvailable
title: IoIsWdmVersionAvailable
author: windows-driver-content
description: The IoIsWdmVersionAvailable routine checks whether a given WDM version is supported by the operating system.
old-location: kernel\ioiswdmversionavailable.htm
old-project: kernel
ms.assetid: 80b72de0-02a6-4891-b74a-c41cb14fa629
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoIsWdmVersionAvailable
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoIsWdmVersionAvailable
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlIoPassive5, PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IoIsWdmVersionAvailable function



## -description
<p>The <b>IoIsWdmVersionAvailable</b> routine checks whether a given WDM version is supported by the operating system.</p>


## -syntax

````
BOOLEAN IoIsWdmVersionAvailable(
  _In_ UCHAR MajorVersion,
  _In_ UCHAR MinorVersion
);
````


## -parameters
<dl>

### -param <i>MajorVersion</i> [in]

<dd>
<p>Specifies the major version number of WDM that is requested.</p>
</dd>

### -param <i>MinorVersion</i> [in]

<dd>
<p>Specifies the minor version number of WDM that is requested.</p>
</dd>
</dl>

## -returns
<p><b>IoIsWdmVersionAvailable</b> returns <b>TRUE</b> if the version of WDM that the operating system provides is greater than or equal to the version number of WDM being requested. Otherwise, it returns <b>FALSE</b>.</p>

## -remarks
<p>Drivers should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561954">RtlIsNtDdiVersionAvailable</a> routine instead of the <b>IoIsWdmVersionAvailable</b> routine.</p>

<p>Cross-platform drivers should use this routine to check the WDM version before performing any operations that vary by platform or are not supported in all versions of WDM.</p>

<p>The WDM_MAJORVERSION and WDM_MINORVERSION constants, which are defined in the Wdm.h header file, specify the WDM major and minor version numbers for the current version of Windows. The following lists the WDM version provided with each operating system.</p>

<p>Windows 7</p>

<p>6</p>

<p>0x00</p>

<p>Windows Server 2008 R2</p>

<p>6</p>

<p>0x00</p>

<p>Windows Server 2008</p>

<p>6</p>

<p>0x00</p>

<p>Windows Vista</p>

<p>6</p>

<p>0x00</p>

<p>Windows Server 2003</p>

<p>1</p>

<p>0x30</p>

<p>Windows XP</p>

<p>1</p>

<p>0x20</p>

<p>Windows 2000</p>

<p>1</p>

<p>0x10</p>

<p>Windows Me</p>

<p>1</p>

<p>0x05</p>

<p>Windows 98</p>

<p>1</p>

<p>0x00</p>

<p> </p>

<p>Note that the minor version number is defined as a hexadecimal value.</p>

<p>Later versions of WDM support all the features available in earlier versions of WDM; that is, each version of WDM is a superset of the previous WDM version.</p>

<p>The following call returns <b>TRUE</b> on any of the listed operating systems, because all these systems support all the features of WDM 1.0:</p>

<p>The following example shows how a driver can dynamically detect the current operating system:</p>

<p>As the example shows, calling <b>IoIsWdmVersionAvailable</b>(1, 5) returns <b>TRUE</b> on Windows Me, Windows 2000, and any succeeding operating systems, but <b>FALSE</b> on Windows 98 and Windows 98 SE.</p>

<p>Drivers should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561954">RtlIsNtDdiVersionAvailable</a> routine instead of the <b>IoIsWdmVersionAvailable</b> routine.</p>

<p>Cross-platform drivers should use this routine to check the WDM version before performing any operations that vary by platform or are not supported in all versions of WDM.</p>

<p>The WDM_MAJORVERSION and WDM_MINORVERSION constants, which are defined in the Wdm.h header file, specify the WDM major and minor version numbers for the current version of Windows. The following lists the WDM version provided with each operating system.</p>

<p>Windows 7</p>

<p>6</p>

<p>0x00</p>

<p>Windows Server 2008 R2</p>

<p>6</p>

<p>0x00</p>

<p>Windows Server 2008</p>

<p>6</p>

<p>0x00</p>

<p>Windows Vista</p>

<p>6</p>

<p>0x00</p>

<p>Windows Server 2003</p>

<p>1</p>

<p>0x30</p>

<p>Windows XP</p>

<p>1</p>

<p>0x20</p>

<p>Windows 2000</p>

<p>1</p>

<p>0x10</p>

<p>Windows Me</p>

<p>1</p>

<p>0x05</p>

<p>Windows 98</p>

<p>1</p>

<p>0x00</p>

<p> </p>

<p>Note that the minor version number is defined as a hexadecimal value.</p>

<p>Later versions of WDM support all the features available in earlier versions of WDM; that is, each version of WDM is a superset of the previous WDM version.</p>

<p>The following call returns <b>TRUE</b> on any of the listed operating systems, because all these systems support all the features of WDM 1.0:</p>

<p>The following example shows how a driver can dynamically detect the current operating system:</p>

<p>As the example shows, calling <b>IoIsWdmVersionAvailable</b>(1, 5) returns <b>TRUE</b> on Windows Me, Windows 2000, and any succeeding operating systems, but <b>FALSE</b> on Windows 98 and Windows 98 SE.</p>

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
<p>Available starting with Windows 2000.</p>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547796">IrqlIoPassive5</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561954">RtlIsNtDdiVersionAvailable</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoIsWdmVersionAvailable routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
