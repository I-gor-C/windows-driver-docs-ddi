---
UID: NS.wdm._OSVERSIONINFOEXW
title: OSVERSIONINFOEXW
author: windows-driver-content
description: The RTL_OSVERSIONINFOEXW structure contains operating system version information.
old-location: kernel\rtl_osversioninfoexw.htm
old-project: kernel
ms.assetid: 88471e00-4913-44fd-b9f4-960ec46fb75a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: OSVERSIONINFOEXW, OSVERSIONINFOEXW, *POSVERSIONINFOEXW, *LPOSVERSIONINFOEXW, RTL_OSVERSIONINFOEXW, *PRTL_OSVERSIONINFOEXW
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RTL_OSVERSIONINFOEXW
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# OSVERSIONINFOEXW structure



## -description
<p>The <b>RTL_OSVERSIONINFOEXW</b> structure contains operating system version information.</p>


## -syntax

````
typedef struct _OSVERSIONINFOEXW {
  ULONG  dwOSVersionInfoSize;
  ULONG  dwMajorVersion;
  ULONG  dwMinorVersion;
  ULONG  dwBuildNumber;
  ULONG  dwPlatformId;
  WCHAR  szCSDVersion[128];
  USHORT wServicePackMajor;
  USHORT wServicePackMinor;
  USHORT wSuiteMask;
  UCHAR  wProductType;
  UCHAR  wReserved;
} RTL_OSVERSIONINFOEXW, *PRTL_OSVERSIONINFOEXW;
````


## -struct-fields
<dl>

### -field dwOSVersionInfoSize

<dd>
<p>The size, in bytes, of an <b>RTL_OSVERSIONINFOEXW</b> structure. This member must be set before the structure is used with <a href="..\wdm\nf-wdm-rtlgetversion.md">RtlGetVersion</a>.</p>
</dd>

### -field dwMajorVersion

<dd>
<p>The major version number of the operating system. For example, for Windows 2000, the major version number is five. For more information, see the table in Remarks.</p>
</dd>

### -field dwMinorVersion

<dd>
<p>The minor version number of the operating system. For example, for Windows 2000, the minor version number is zero. For more information, see the table in Remarks.</p>
</dd>

### -field dwBuildNumber

<dd>
<p>The build number of the operating system.</p>
</dd>

### -field dwPlatformId

<dd>
<p>The operating system platform. For Win32 on NT-based operating systems, <b>RtlGetVersion</b> returns the value VER_PLATFORM_WIN32_NT.</p>
</dd>

### -field szCSDVersion

<dd>
<p>The service-pack version string. This member contains a null-terminated string, such as "Service Pack 3", which indicates the latest service pack installed on the system. If no service pack is installed, <b>RtlGetVersion</b> might not initialize this string. Initialize <i>szCSDVersion</i> to zero (empty string) before the call to <b>RtlGetVersion</b>.</p>
</dd>

### -field wServicePackMajor

<dd>
<p>The major version number of the latest service pack installed on the system. For example, for Service Pack 3, the major version number is three. If no service pack has been installed, the value is zero.</p>
</dd>

### -field wServicePackMinor

<dd>
<p>The minor version number of the latest service pack installed on the system. For example, for Service Pack 3, the minor version number is zero.</p>
</dd>

### -field wSuiteMask

<dd>
<p>The product suites available on the system. This member is set to zero or to the bitwise OR of one or more of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>VER_SUITE_BACKOFFICE</p>
</td>
<td>
<p>Microsoft BackOffice components are installed.</p>
</td>
</tr>
<tr>
<td>
<p>VER_SUITE_BLADE</p>
</td>
<td>
<p>Windows Server 2003, Web Edition is installed.</p>
</td>
</tr>
<tr>
<td>
<p>VER_SUITE_COMPUTE_SERVER</p>
</td>
<td>
<p>Windows Server 2003, Compute Cluster Edition is installed.</p>
</td>
</tr>
<tr>
<td>
<p>VER_SUITE_DATACENTER</p>
</td>
<td>
<p>Windows Server 2008 Datacenter, Windows Server 2003, Datacenter Edition, or Windows 2000 Datacenter Server is installed.</p>
</td>
</tr>
<tr>
<td>
<p>VER_SUITE_ENTERPRISE</p>
</td>
<td>
<p>Windows Server 2008 Enterprise, Windows Server 2003, Enterprise Edition, or Windows 2000 Advanced Server is installed.</p>
</td>
</tr>
<tr>
<td>
<p>VER_SUITE_EMBEDDEDNT</p>
</td>
<td>
<p>Windows XP Embedded is installed.</p>
</td>
</tr>
<tr>
<td>
<p>VER_SUITE_PERSONAL</p>
</td>
<td>
<p>Windows Vista Home Premium, Windows Vista Home Basic, or Windows XP Home Edition is installed.</p>
</td>
</tr>
<tr>
<td>
<p>VER_SUITE_SINGLEUSERTS</p>
</td>
<td>
<p>Remote Desktop is supported, but only one interactive session is supported. This value is set unless the system is running in application server mode.</p>
</td>
</tr>
<tr>
<td>
<p>VER_SUITE_SMALLBUSINESS (see note)</p>
</td>
<td>
<p>Microsoft Small Business Server was once installed on the system, but may have been upgraded to another version of Windows. For more information about this flag bit, see the following Remarks section.</p>
</td>
</tr>
<tr>
<td>
<p>VER_SUITE_SMALLBUSINESS_RESTRICTED</p>
</td>
<td>
<p>Microsoft Small Business Server is installed with the restrictive client license in force. For more information about this flag bit, see the following Remarks section.</p>
</td>
</tr>
<tr>
<td>
<p>VER_SUITE_STORAGE_SERVER</p>
</td>
<td>
<p>Windows Storage Server 2003 R2 or Windows Storage Server 2003 is installed.</p>
</td>
</tr>
<tr>
<td>
<p>VER_SUITE_TERMINAL</p>
</td>
<td>
<p>Terminal Services is installed. This value is always set.</p>
<p>If VER_SUITE_TERMINAL is set but VER_SUITE_SINGLEUSERTS is not set, the operating system is running in application server mode.</p>
</td>
</tr>
<tr>
<td>
<p>VER_SUITE_WH_SERVER</p>
</td>
<td>
<p>Windows Home Server is installed.</p>
</td>
</tr>
</table>
<p> </p>
<div class="alert"><b>Note</b>    You should not rely solely on the VER_SUITE_SMALLBUSINESS flag to determine whether Small Business Server is currently installed. Both this flag and the VER_SUITE_SMALLBUSINESS_RESTRICTED flag are set when this product suite is installed. If you upgrade this installation to Windows Server, Standard Edition, the VER_SUITE_SMALLBUSINESS_RESTRICTED flag is cleared, but the VER_SUITE_SMALLBUSINESS flag remains set, which, in this case, indicates that Small Business Server was previously installed on this system. If this installation is further upgraded to Windows Server, Enterprise Edition, the VER_SUITE_SMALLBUSINESS flag remains set.</div>
<div> </div>
</dd>

### -field wProductType

<dd>
<p>The product type. This member contains additional information about the system. This member can be one of the following values: </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>VER_NT_WORKSTATION</p>
</td>
<td>
<p>Windows 2000 or later professional version</p>
</td>
</tr>
<tr>
<td>
<p>VER_NT_DOMAIN_CONTROLLER</p>
</td>
<td>
<p>Windows 2000 or later domain controller</p>
</td>
</tr>
<tr>
<td>
<p>VER_NT_SERVER</p>
</td>
<td>
<p>Windows 2000 or later server</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field wReserved

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>

## -remarks
<p>The information in this structure includes the major and minor version numbers, the build number, the platform identifier, the installed product suites, and the latest service pack that is installed on the system. This structure is used with the <a href="..\wdm\nf-wdm-rtlgetversion.md">RtlGetVersion</a> and <a href="..\wdm\nf-wdm-rtlverifyversioninfo.md">RtlVerifyVersionInfo</a> routines.</p>

<p>Relying on version information is not always the best way to test whether a feature is available. For guidance, refer to the documentation for the feature you are interested in.</p>

<p>If possible, design the version detection code in your driver to enable the driver to run on future versions of Windows. If your driver requires a particular operating system version, be sure to treat this version as the minimum supported version, and not as the only version on which the driver can run.</p>

<p>The following table summarizes the version information that is returned by supported versions of Windows. Use the information in the "Other" column to distinguish between operating systems with identical version numbers.</p>

<p>Windows 8.1</p>

<p>6.3</p>

<p>6</p>

<p>3</p>

<p><b>wProductType</b> == VER_NT_WORKSTATION</p>

<p>Windows 8</p>

<p>6.2</p>

<p>2</p>

<p>Windows Server 2012</p>

<p><b>wProductType</b> != VER_NT_WORKSTATION</p>

<p>Windows 7</p>

<p>6.1</p>

<p>1</p>

<p>Windows Server 2008 R2</p>

<p>Windows Server 2008</p>

<p>6.0</p>

<p>0</p>

<p>Windows Vista</p>

<p>Windows Home Server</p>

<p>5.2</p>

<p>5</p>

<p><b>wSuiteMask</b> == VER_SUITE_WH_SERVER</p>

<p>Windows Server 2003</p>

<p>Not applicable</p>

<p>Windows XP Professional x64 Edition (see note)</p>

<p><b>wProductType</b> == VER_NT_WORKSTATION </p>

<p>Windows XP</p>

<p>5.1</p>

<p>Windows 2000</p>

<p>5.0</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="kernel.rtl_osversioninfow">RTL_OSVERSIONINFOW</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-rtlgetversion.md">RtlGetVersion</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-rtlverifyversioninfo.md">RtlVerifyVersionInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RTL_OSVERSIONINFOEXW structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
