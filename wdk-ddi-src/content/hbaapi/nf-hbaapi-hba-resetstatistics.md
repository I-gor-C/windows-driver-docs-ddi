---
UID: NF.hbaapi.HBA_ResetStatistics
title: HBA_ResetStatistics
author: windows-driver-content
description: The HBA_ResetStatistics routine resets the statistics counters for the indicated port and HBA.
old-location: storage\hba_resetstatistics.htm
old-project: storage
ms.assetid: 4e889905-9c5e-446c-8d0e-09e445f7c1a4
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: HBA_ResetStatistics
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBA_ResetStatistics
req.alt-loc: Hbaapi.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hbaapi.lib
req.dll: Hbaapi.dll
req.irql: 
req.iface: 
---

# HBA_ResetStatistics function



## -description
<p>The <b>HBA_ResetStatistics</b> routine resets the statistics counters for the indicated port and HBA. </p>


## -syntax

````
void HBA_API HBA_ResetStatistics(
  _In_ HBA_HANDLE HbaHandle,
  _In_ HBA_UINT32 PortIndex
);
````


## -parameters
<dl>

### -param HbaHandle [in]

<dd>
<p>Contains a value returned by the routine <a href="..\hbaapi\nf-hbaapi-hba-openadapter.md">HBA_OpenAdapter</a> that identifies the HBA on which the port is located.  </p>
</dd>

### -param PortIndex [in]

<dd>
<p>Indicates for which port on the HBA the statistics counters should be reset. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>HBA_ResetStatistics</b> routine serves similar purpose to the <b>ResetStatistics</b> method of the <a href="storage.msfc_fibreporthbamethods_wmi_class">MSFC_FibrePortHBAMethods WMI Class</a>. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.h (include Hbaapi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\hbaapi\nf-hbaapi-hba-openadapter.md">HBA_OpenAdapter</a>
</dt>
<dt>
<a href="storage.msfc_fibreporthbamethods_wmi_class">MSFC_FibrePortHBAMethods WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HBA_ResetStatistics routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
