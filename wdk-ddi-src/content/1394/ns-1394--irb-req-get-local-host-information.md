---
UID: NS.1394._IRB_REQ_GET_LOCAL_HOST_INFORMATION
title: IRB_REQ_GET_LOCAL_HOST_INFORMATION
author: windows-driver-content
description: This structure contains the fields necessary for the 1394 bus driver to carry out a GetLocalHostInformation request.
old-location: ieee\irb_req_get_local_host_information.htm
ms.assetid: 172579A1-9B81-42C7-BAC9-C977C69E7E45
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: IEEE
req.header: 1394.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRB_REQ_GET_LOCAL_HOST_INFORMATION
req.alt-loc: 1394.h
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
ms.keywords: IRB_REQ_GET_LOCAL_HOST_INFORMATION, IRB_REQ_GET_LOCAL_HOST_INFORMATION
---

# IRB_REQ_GET_LOCAL_HOST_INFORMATION structure



## -description
<p>This structure contains the fields necessary for the 1394 bus driver to carry out a GetLocalHostInformation request.</p>


## -syntax

````
typedef struct _IRB_REQ_GET_LOCAL_HOST_INFORMATION {
  ULONG nLevel;
  PVOID Information;
} IRB_REQ_GET_LOCAL_HOST_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>nLevel</b>

<dd>
<p>Specifies what level of information is desired from this call. The following flags are provided.</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p> GET_HOST_UNIQUE_ID </p>
</td>
<td>
<p>Requests the port driver to return the 64-bit unique identifier. </p>
</td>
</tr>
<tr>
<td>
<p>GET_HOST_CAPABILITIES</p>
</td>
<td>
<p>Requests the port driver to return the host controller's capability flags.</p>
</td>
</tr>
<tr>
<td>
<p>GET_HOST_DDI_VERSION</p>
</td>
<td>
<p>Requests the DDI version of the 1394 bus driver.</p>
</td>
</tr>
<tr>
<td>
<p>GET_POWER_SUPPLIED</p>
</td>
<td>
<p>Requests the port driver to return the power characteristics of the bus.</p>
</td>
</tr>
<tr>
<td>
<p>GET_PHYS_ADDR_ROUTINE</p>
</td>
<td>
<p>Requests the port driver to return the host controller's physical address mapping function. </p>
</td>
</tr>
<tr>
<td>
<p>GET_HOST_CONFIG_ROM</p>
</td>
<td>
<p>Requests the port driver to return the host controller's configuration ROM.</p>
</td>
</tr>
<tr>
<td>
<p>GET_HOST_CSR_CONTENTS</p>
</td>
<td>
<p>Requests the port driver to return the speed or topology maps from the host controller's CSR. See the IEEE 1394 Specification for a description of CSRs.<div class="alert"><b>Note</b>  In Windows 7, setting <b>nLevel</b> to GET_HOST_CSR_CONTENTS and specifying the SPEED_MAP_LOCATION as <b>CsrBaseAddress</b> is not supported. The speed map is obsolete in the IEEE-1394a specification.</div>
<div> </div>
</p>
</td>
</tr>
<tr>
<td>
<p>GET_HOST_DMA_CAPABILITIES</p>
</td>
<td>
<p>Requests the port driver to return the host controller's capability flags and the size of the DMA buffer (PAGESIZE multiplied by the number of mapping registers).</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Information</b>

<dd>
<p>Points to an information block to be filled in, depending on what level of information is desired. Each block has its own particular structure.</p>
<table>
<tr>
<th>Flag</th>
<th>Structure</th>
</tr>
<tr>
<td>
<p>GET_HOST_UNIQUE_ID</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537146">GET_LOCAL_HOST_INFO1</a>
</p>
</td>
</tr>
<tr>
<td>
<p>GET_HOST_CAPABILITIES</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537147">GET_LOCAL_HOST_INFO2</a>
</p>
</td>
</tr>
<tr>
<td>
<p>GET_POWER_SUPPLIED</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537149">GET_LOCAL_HOST_INFO3</a>
</p>
</td>
</tr>
<tr>
<td>
<p>GET_PHYS_ADDR_ROUTINE</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537151">GET_LOCAL_HOST_INFO4</a>
</p>
</td>
</tr>
<tr>
<td>
<p>GET_HOST_CONFIG_ROM</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537152">GET_LOCAL_HOST_INFO5</a>
</p>
</td>
</tr>
<tr>
<td>
<p>GET_HOST_CSR_CONTENTS</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537155">GET_LOCAL_HOST_INFO6</a>
</p>
</td>
</tr>
<tr>
<td>
<p>GET_HOST_DMA_CAPABILITIES</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537157">GET_LOCAL_HOST_INFO7</a>
</p>
</td>
</tr>
<tr>
<td>
<p>GET_HOST_DDI_VERSION</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/gg266401">GET_LOCAL_HOST_INFO8</a>
</p>
</td>
</tr>
</table>
<p> </p>
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
<dt>1394.h</dt>
</dl>
</td>
</tr>
</table>