---
UID : NE:d3dkmthk._D3DKMT_VIDMMESCAPETYPE
title : _D3DKMT_VIDMMESCAPETYPE
author : windows-driver-content
description : The D3DKMT_VIDMMESCAPETYPE enumeration is used with the D3DKMT_VIDMM_ESCAPE structure.
old-location : display\d3dkmt_vidmmescapetype.htm
old-project : display
ms.assetid : 83C903F9-0E5F-454D-B6E9-FCC7C3A9B46C
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3DKMT_VIDMMESCAPETYPE, D3DKMT_VIDMMESCAPETYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3dkmthk.h
req.include-header : TBD
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3DKMT_VIDMMESCAPETYPE
req.alt-loc : d3dkmthk.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : D3DKMT_VIDMMESCAPETYPE
---

# _D3DKMT_VIDMMESCAPETYPE Enumeration
<b>Do not use the D3DKMT_VIDMMESCAPETYPE enumeration; it is for testing purposes only.</b>

The D3DKMT_VIDMMESCAPETYPE enumeration is used with the <a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_vidmm_escape.md">D3DKMT_VIDMM_ESCAPE</a> structure.

## Syntax
````
typedef enum _D3DKMT_VIDMMESCAPETYPE { 
  D3DKMT_VIDMMESCAPETYPE_SETFAULT                      = 0,
  D3DKMT_VIDMMESCAPETYPE_RUN_COHERENCY_TEST            = 1,
  D3DKMT_VIDMMESCAPETYPE_RUN_UNMAP_TO_DUMMY_PAGE_TEST  = 2,
  D3DKMT_VIDMMESCAPETYPE_APERTURE_CORRUPTION_CHECK     = 3,
  D3DKMT_VIDMMESCAPETYPE_SUSPEND_CPU_ACCESS_TEST       = 4,
  D3DKMT_VIDMMESCAPETYPE_EVICT                         = 5,
  D3DKMT_VIDMMESCAPETYPE_EVICT_BY_NT_HANDLE            = 6,
  D3DKMT_VIDMMESCAPETYPE_GET_VAD_INFO                  = 7,
  D3DKMT_VIDMMESCAPETYPE_SET_BUDGET                    = 8,
  D3DKMT_VIDMMESCAPETYPE_SUSPEND_PROCESS               = 9,
  D3DKMT_VIDMMESCAPETYPE_RESUME_PROCESS                = 10,
  D3DKMT_VIDMMESCAPETYPE_GET_BUDGET                    = 11,
  D3DKMT_VIDMMESCAPETYPE_SET_TRIM_INTERVALS            = 12,
  D3DKMT_VIDMMESCAPETYPE_EVICT_BY_CRITERIA             = 13
} D3DKMT_VIDMMESCAPETYPE;
````

## Constants

<table>

<tr>
<td>D3DKMT_VIDMMESCAPETYPE_APERTURE_CORRUPTION_CHECK</td>
<td></td>
</tr>

<tr>
<td>D3DKMT_VIDMMESCAPETYPE_EVICT</td>
<td></td>
</tr>

<tr>
<td>D3DKMT_VIDMMESCAPETYPE_EVICT_BY_CRITERIA</td>
<td></td>
</tr>

<tr>
<td>D3DKMT_VIDMMESCAPETYPE_EVICT_BY_NT_HANDLE</td>
<td></td>
</tr>

<tr>
<td>D3DKMT_VIDMMESCAPETYPE_GET_BUDGET</td>
<td></td>
</tr>

<tr>
<td>D3DKMT_VIDMMESCAPETYPE_GET_VAD_INFO</td>
<td></td>
</tr>

<tr>
<td>D3DKMT_VIDMMESCAPETYPE_RESUME_PROCESS</td>
<td></td>
</tr>

<tr>
<td>D3DKMT_VIDMMESCAPETYPE_RUN_COHERENCY_TEST</td>
<td></td>
</tr>

<tr>
<td>D3DKMT_VIDMMESCAPETYPE_RUN_UNMAP_TO_DUMMY_PAGE_TEST</td>
<td></td>
</tr>

<tr>
<td>D3DKMT_VIDMMESCAPETYPE_SET_BUDGET</td>
<td></td>
</tr>

<tr>
<td>D3DKMT_VIDMMESCAPETYPE_SET_TRIM_INTERVALS</td>
<td></td>
</tr>

<tr>
<td>D3DKMT_VIDMMESCAPETYPE_SETFAULT</td>
<td></td>
</tr>

<tr>
<td>D3DKMT_VIDMMESCAPETYPE_SUSPEND_CPU_ACCESS_TEST</td>
<td></td>
</tr>

<tr>
<td>D3DKMT_VIDMMESCAPETYPE_SUSPEND_PROCESS</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmthk.h (include TBD) |