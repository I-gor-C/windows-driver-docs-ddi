---
UID: NC.wlanihv.DOT11EXTIHV_INIT_SERVICE
title: DOT11EXTIHV_INIT_SERVICE
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extihvinitservice.htm
ms.assetid: ba803eab-74ae-4998-b013-9f4470da8382
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: wlanihv.h
req.include-header: Wlanihv.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Dot11ExtIhvInitService
req.alt-loc: wlanihv.h
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
ms.keywords: PrintPropertyValue, PrintPropertyValue
req.iface: 
req.product: Windows 10 or later.
---

# DOT11EXTIHV_INIT_SERVICE callback



## -description

## -prototype

````
DOT11EXTIHV_INIT_SERVICE Dot11ExtIhvInitService;

DWORD APIENTRY Dot11ExtIhvInitService(
  _In_       DWORD                  dwVerNumUsed,
  _In_       PDOT11EXT_APIS         pDot11ExtAPI,
  _Reserved_ LPVOID                 pvReserved,
  _Out_      PDOT11EXT_IHV_HANDLERS pDot11IHVHandlers
)
{ ... }
````


## -parameters
<dl>

### -param <i>dwVerNumUsed</i> [in]

<dd>
<p>The interface version used by the operating system. The value of this parameter must be between
     the ranges of version numbers returned in the 
     <i>pDot11IHVVersionInfo</i> parameter of the 
     <a href="https://msdn.microsoft.com/af75e59d-c4af-43ca-a160-ddc8a7a4a88e">
     Dot11ExtIhvGetVersionInfo</a> IHV Handler function.</p>
</dd>

### -param <i>pDot11ExtAPI</i> [in]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff547617">DOT11EXT_APIS</a> structure, which contains the
     addresses of the IHV Extensibility functions that are supported by the operating system. The operating
     system formats this parameter with the function addresses before making the call to the 
     <i>Dot11ExtIhvInitService</i> function.</p>
</dd>

### -param <i>pvReserved</i> 

<dd>
<p>This parameter is reserved for use by the operating system.</p>
</dd>

### -param <i>pDot11IHVHandlers</i> [out]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff547625">DOT11EXT_IHV_HANDLERS</a> structure,
     which contains the addresses of the IHV Handler functions supported by the IHV Extensions DLL. The DLL
     formats this parameter with the function addresses before returning from the call to the 
     <i>Dot11ExtIhvInitService</i> function.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.</p>

## -remarks
<p>The operating system calls the 
    <i>Dot11ExtIhvInitService</i> function immediately after the call to the 
    <a href="https://msdn.microsoft.com/af75e59d-c4af-43ca-a160-ddc8a7a4a88e">
    Dot11ExtIhvGetVersionInfo</a> function. When called, 
    <i>Dot11ExtIhvInitService</i> must initialize the IHV Extensions DLL as necessary. When the function
    returns, the DLL must be prepared to accept additional calls to the IHV Handler function.</p>

<p>Unlike how it treats other IHV Extension and Handler functions whose addresses are resolved through
    the 
    <i>pDot11IHVHandlers</i> parameter, the operating system resolves the address of the 
    <i>Dot11ExtIhvInitService</i> function by calling the 
    <b>GetProcAddress</b> function. As a result, the developer of the IHV Extensions DLL must follow these
    guidelines.</p>

<p>The DLL must implement a function named Dot11ExtIhvInitService, which has the format that is
      described in this topic.</p>

<p>The 
      <b>EXPORTS</b> statement of the source module-definition (.def) file, which is used to build the IHV
      Extensions DLL, must contain a function name entry for the 
      <i>Dot11ExtIhvInitService</i> function.</p>

<p>For more information about 
    <b>GetProcAddress</b>, refer to the Microsoft Windows SDK documentation.</p>

<p>The operating system calls the 
    <i>Dot11ExtIhvInitService</i> function immediately after the call to the 
    <a href="https://msdn.microsoft.com/af75e59d-c4af-43ca-a160-ddc8a7a4a88e">
    Dot11ExtIhvGetVersionInfo</a> function. When called, 
    <i>Dot11ExtIhvInitService</i> must initialize the IHV Extensions DLL as necessary. When the function
    returns, the DLL must be prepared to accept additional calls to the IHV Handler function.</p>

<p>Unlike how it treats other IHV Extension and Handler functions whose addresses are resolved through
    the 
    <i>pDot11IHVHandlers</i> parameter, the operating system resolves the address of the 
    <i>Dot11ExtIhvInitService</i> function by calling the 
    <b>GetProcAddress</b> function. As a result, the developer of the IHV Extensions DLL must follow these
    guidelines.</p>

<p>The DLL must implement a function named Dot11ExtIhvInitService, which has the format that is
      described in this topic.</p>

<p>The 
      <b>EXPORTS</b> statement of the source module-definition (.def) file, which is used to build the IHV
      Extensions DLL, must contain a function name entry for the 
      <i>Dot11ExtIhvInitService</i> function.</p>

<p>For more information about 
    <b>GetProcAddress</b>, refer to the Microsoft Windows SDK documentation.</p>

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
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wlanihv.h (include Wlanihv.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547617">DOT11EXT_APIS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547625">DOT11EXT_IHV_HANDLERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/af75e59d-c4af-43ca-a160-ddc8a7a4a88e">Dot11ExtIhvGetVersionInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXTIHV_INIT_SERVICE callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
