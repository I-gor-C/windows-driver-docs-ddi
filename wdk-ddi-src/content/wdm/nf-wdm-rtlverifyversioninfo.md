---
UID: NF.wdm.RtlVerifyVersionInfo
title: RtlVerifyVersionInfo
author: windows-driver-content
description: The RtlVerifyVersionInfo routine compares a specified set of operating system version requirements to the corresponding attributes of the currently running version of the operating system.
old-location: kernel\rtlverifyversioninfo.htm
old-project: kernel
ms.assetid: 7c0ca9a0-dfa4-44ab-8d3a-ab43f72c806f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlVerifyVersionInfo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlVerifyVersionInfo
req.alt-loc: NtosKrnl.exe,Ntdll.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode); Ntdll.dll (user mode)
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# RtlVerifyVersionInfo function



## -description
<p>The <b>RtlVerifyVersionInfo</b> routine compares a specified set of operating system version requirements to the corresponding attributes of the currently running version of the operating system.</p>


## -syntax

````
NTSTATUS RtlVerifyVersionInfo(
  _In_ PRTL_OSVERSIONINFOEXW VersionInfo,
  _In_ ULONG                 TypeMask,
  _In_ ULONGLONG             ConditionMask
);
````


## -parameters
<dl>

### -param VersionInfo [in]

<dd>
<p>Pointer to an <a href="kernel.rtl_osversioninfoexw">RTL_OSVERSIONINFOEXW</a> structure that specifies the operating system version requirements to compare to the corresponding attributes of the currently running version of the operating system. </p>
</dd>

### -param TypeMask [in]

<dd>
<p>Specifies which members of <i>VersionInfo</i> to compare with the corresponding attributes of the currently running version of the operating system. <i>TypeMask</i> is set to a logical OR of one or more of the following values.
                        </p>
<table>
<tr>
<th>Value</th>
<th>Corresponding member</th>
</tr>
<tr>
<td>
<p>VER_BUILDNUMBER</p>
</td>
<td>
<p><b>dwBuildNumber</b></p>
</td>
</tr>
<tr>
<td>
<p>VER_MAJORVERSION</p>
</td>
<td>
<p><b>dwMajorVersion</b></p>
</td>
</tr>
<tr>
<td>
<p>VER_MINORVERSION</p>
</td>
<td>
<p><b>dwMinorVersion</b></p>
</td>
</tr>
<tr>
<td>
<p>VER_PLATFORMID</p>
</td>
<td>
<p><b>dwPlatformId</b></p>
</td>
</tr>
<tr>
<td>
<p>VER_SERVICEPACKMAJOR</p>
</td>
<td>
<p><b>wServicePackMajor</b></p>
</td>
</tr>
<tr>
<td>
<p>VER_SERVICEPACKMINOR</p>
</td>
<td>
<p><b>wServicePackMinor</b></p>
</td>
</tr>
<tr>
<td>
<p>VER_SUITENAME</p>
</td>
<td>
<p><b>wSuiteMask</b></p>
</td>
</tr>
<tr>
<td>
<p>VER_PRODUCT_TYPE</p>
</td>
<td>
<p><b>wProductType</b></p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param ConditionMask [in]

<dd>
<p>Specifies how to compare each <b>VersionInfo</b> member. To set the value of <i>ConditionMask</i>, a caller should use the <b>VER_SET_CONDITION</b> macro:
						  </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>VER_SET_CONDITION (
        IN OUT  ULONGLONG  ConditionMask,
        IN ULONG  TypeBitMask,
        IN UCHAR  ComparisonType
        );</pre>
</td>
</tr>
</table></span></div>
<p>The value of <i>ConditionMask</i> is created in the following way:</p>
<ul>
<li>
<p>Initialize the value of <i>ConditionMask</i> to zero. </p>
</li>
<li>
<p>Call <b>VER_SET_CONDITION</b> once for each <i>VersionInfo</i> member specified by <i>TypeMask</i>.</p>
</li>
<li>
<p>Set the <i>TypeBitMask</i> and <i>ComparisonType</i> parameters for each call to <b>VER_SET_CONDITION</b> as follows:</p>
</li>
</ul>
<p></p>
<dl>

### -param TypeBitMask

<dd>
<p>Indicates the <i>VersionInfo</i> member for which the comparison type is set. <i>TypeBitMask</i> can be one of the following values.
        </p>
<table>
<tr>
<th>Value</th>
<th>Corresponding member</th>
</tr>
<tr>
<td>
<p>VER_BUILDNUMBER</p>
</td>
<td>
<p><b>dwBuildNumber</b></p>
</td>
</tr>
<tr>
<td>
<p>VER_MAJORVERSION</p>
</td>
<td>
<p><b>dwMajorVersion</b></p>
</td>
</tr>
<tr>
<td>
<p>VER_MINORVERSION</p>
</td>
<td>
<p><b>dwMinorVersion</b></p>
</td>
</tr>
<tr>
<td>
<p>VER_PLATFORMID</p>
</td>
<td>
<p><b>dwPlatformId</b></p>
</td>
</tr>
<tr>
<td>
<p>VER_SERVICEPACKMAJOR</p>
</td>
<td>
<p><b>wServicePackMajor</b></p>
</td>
</tr>
<tr>
<td>
<p>VER_SERVICEPACKMINOR</p>
</td>
<td>
<p><b>wServicePackMinor</b></p>
</td>
</tr>
<tr>
<td>
<p>VER_SUITENAME</p>
</td>
<td>
<p><b>wSuiteMask</b></p>
</td>
</tr>
<tr>
<td>
<p>VER_PRODUCT_TYPE</p>
</td>
<td>
<p><b>wProductType</b></p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param ComparisonType

<dd>
<p>Specifies the comparison type that <b>RtlVerifyVersionInfo</b> uses to compare the <b>VersionInfo</b> member specified by <i>TypeBitMask</i> with the corresponding attribute of the currently running operating system.
        </p>
<p>For all values of <i>TypeBitMask</i> other than VER_SUITENAME, <i>ComparisonType</i> is set to one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>VER_EQUAL</p>
</td>
<td>
<p>The current value must be equal to the specified value.</p>
</td>
</tr>
<tr>
<td>
<p>VER_GREATER</p>
</td>
<td>
<p>The current value must be greater than the specified value.</p>
</td>
</tr>
<tr>
<td>
<p>VER_GREATER_EQUAL</p>
</td>
<td>
<p>The current value must be greater than or equal to the specified value.</p>
</td>
</tr>
<tr>
<td>
<p>VER_LESS</p>
</td>
<td>
<p>The current value must be less than the specified value.</p>
</td>
</tr>
<tr>
<td>
<p>VER_LESS_EQUAL</p>
</td>
<td>
<p>The current value must be less than or equal to the specified value.</p>
</td>
</tr>
</table>
<p> </p>
<p>If <i>TypeBitMask</i> is set to VER_SUITENAME, <i>ComparisonType</i> is set to of one the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>VER_AND</p>
</td>
<td>
<p>All product suites specified in the <b>wSuiteMask</b> member must be present in the current system.</p>
</td>
</tr>
<tr>
<td>
<p>VER_OR</p>
</td>
<td>
<p>At least one of the specified product suites must be present in the current system.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p><b>RtlVerifyVersionInfo</b> returns one of the following status values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The specified version matches the currently running version of the operating system.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The input parameters are not valid.</p><dl>
<dt><b>STATUS_REVISION_MISMATCH</b></dt>
</dl><p>The specified version does not match the currently running version of the operating system.</p>

<p> </p>

## -remarks
<p><b>RtlVerifyVersionInfo</b> enables a driver to easily verify the presence of a required set of operating system attributes. <b>RtlVerifyVersionInfo</b> is the kernel-mode equivalent of the user-mode <b>VerifyVersionInfo</b> function in the Windows SDK. See the example in the Windows SDK that shows how to verify the system version.</p>

<p>Typically, <b>RtlVerifyVersionInfo</b> returns STATUS_SUCCESS only if all comparisons succeed. However, the major version, minor version, and service pack version are tested in a sequential manner in the following way:</p>

<p>If the major version exceeds the minimum required, then the minor version and service pack version are not tested. For example, if the current major version is 6.0, a test for a system greater than or equal to version 5.1 service pack 1 succeeds. The minor version and service pack version are not tested.</p>

<p>If the minor version exceeds the minimum required, then the service pack version is not tested. For example, if the current major version is 5.2, a test for a system version greater than or equal to version 5.1 service pack 1 succeeds. The service pack version is not tested.</p>

<p>If the major service pack version exceeds the minimum required, then the minor service pack version is not tested.</p>

<p>To verify a range of system versions, a driver can call <b>RtlVerifyVersionInfo</b> twice, once to verify a lower bound on the system version and once to verify an upper bound on the system version.</p>

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
<p>Available in Windows 2000 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Ntddk.h)</dt>
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
<dt>NtosKrnl.exe (kernel mode); </dt>
<dt>Ntdll.dll (user mode)</dt>
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
<a href="..\wdm\nf-wdm-rtlgetversion.md">RtlGetVersion</a>
</dt>
<dt>
<a href="kernel.rtl_osversioninfow">RTL_OSVERSIONINFOW</a>
</dt>
<dt>
<a href="kernel.rtl_osversioninfoexw">RTL_OSVERSIONINFOEXW</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlVerifyVersionInfo routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
