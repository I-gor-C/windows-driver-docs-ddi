---
UID: NE.d3dkmthk._D3DKMT_VIDMMESCAPETYPE
title: D3DKMT_VIDMMESCAPETYPE
author: windows-driver-content
description: The D3DKMT_VIDMMESCAPETYPE enumeration is used with the D3DKMT_VIDMM_ESCAPE structure.
old-location: display\d3dkmt_vidmmescapetype.htm
old-project: display
ms.assetid: 83C903F9-0E5F-454D-B6E9-FCC7C3A9B46C
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmthk.h
req.include-header: TBD
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_VIDMMESCAPETYPE
req.alt-loc: d3dkmthk.h
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

# D3DKMT_VIDMMESCAPETYPE enumeration



## -description
<p><b>Do not use the D3DKMT_VIDMMESCAPETYPE enumeration; it is for testing purposes only.</b></p>
<p>The D3DKMT_VIDMMESCAPETYPE enumeration is used with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548410">D3DKMT_VIDMM_ESCAPE</a> structure.</p>


## -syntax

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


## -enum-fields
<dl>

### -field <a id="D3DKMT_VIDMMESCAPETYPE_SETFAULT"></a><a id="d3dkmt_vidmmescapetype_setfault"></a><b>D3DKMT_VIDMMESCAPETYPE_SETFAULT</b>

<dd></dd>

### -field <a id="D3DKMT_VIDMMESCAPETYPE_RUN_COHERENCY_TEST"></a><a id="d3dkmt_vidmmescapetype_run_coherency_test"></a><b>D3DKMT_VIDMMESCAPETYPE_RUN_COHERENCY_TEST</b>

<dd></dd>

### -field <a id="D3DKMT_VIDMMESCAPETYPE_RUN_UNMAP_TO_DUMMY_PAGE_TEST"></a><a id="d3dkmt_vidmmescapetype_run_unmap_to_dummy_page_test"></a><b>D3DKMT_VIDMMESCAPETYPE_RUN_UNMAP_TO_DUMMY_PAGE_TEST</b>

<dd></dd>

### -field <a id="D3DKMT_VIDMMESCAPETYPE_APERTURE_CORRUPTION_CHECK"></a><a id="d3dkmt_vidmmescapetype_aperture_corruption_check"></a><b>D3DKMT_VIDMMESCAPETYPE_APERTURE_CORRUPTION_CHECK</b>

<dd></dd>

### -field <a id="D3DKMT_VIDMMESCAPETYPE_SUSPEND_CPU_ACCESS_TEST"></a><a id="d3dkmt_vidmmescapetype_suspend_cpu_access_test"></a><b>D3DKMT_VIDMMESCAPETYPE_SUSPEND_CPU_ACCESS_TEST</b>

<dd></dd>

### -field <a id="D3DKMT_VIDMMESCAPETYPE_EVICT"></a><a id="d3dkmt_vidmmescapetype_evict"></a><b>D3DKMT_VIDMMESCAPETYPE_EVICT</b>

<dd></dd>

### -field <a id="D3DKMT_VIDMMESCAPETYPE_EVICT_BY_NT_HANDLE"></a><a id="d3dkmt_vidmmescapetype_evict_by_nt_handle"></a><b>D3DKMT_VIDMMESCAPETYPE_EVICT_BY_NT_HANDLE</b>

<dd></dd>

### -field <a id="D3DKMT_VIDMMESCAPETYPE_GET_VAD_INFO"></a><a id="d3dkmt_vidmmescapetype_get_vad_info"></a><b>D3DKMT_VIDMMESCAPETYPE_GET_VAD_INFO</b>

<dd></dd>

### -field <a id="D3DKMT_VIDMMESCAPETYPE_SET_BUDGET"></a><a id="d3dkmt_vidmmescapetype_set_budget"></a><b>D3DKMT_VIDMMESCAPETYPE_SET_BUDGET</b>

<dd></dd>

### -field <a id="D3DKMT_VIDMMESCAPETYPE_SUSPEND_PROCESS"></a><a id="d3dkmt_vidmmescapetype_suspend_process"></a><b>D3DKMT_VIDMMESCAPETYPE_SUSPEND_PROCESS</b>

<dd></dd>

### -field <a id="D3DKMT_VIDMMESCAPETYPE_RESUME_PROCESS"></a><a id="d3dkmt_vidmmescapetype_resume_process"></a><b>D3DKMT_VIDMMESCAPETYPE_RESUME_PROCESS</b>

<dd></dd>

### -field <a id="D3DKMT_VIDMMESCAPETYPE_GET_BUDGET"></a><a id="d3dkmt_vidmmescapetype_get_budget"></a><b>D3DKMT_VIDMMESCAPETYPE_GET_BUDGET</b>

<dd></dd>

### -field <a id="D3DKMT_VIDMMESCAPETYPE_SET_TRIM_INTERVALS"></a><a id="d3dkmt_vidmmescapetype_set_trim_intervals"></a><b>D3DKMT_VIDMMESCAPETYPE_SET_TRIM_INTERVALS</b>

<dd></dd>

### -field <a id="D3DKMT_VIDMMESCAPETYPE_EVICT_BY_CRITERIA"></a><a id="d3dkmt_vidmmescapetype_evict_by_criteria"></a><b>D3DKMT_VIDMMESCAPETYPE_EVICT_BY_CRITERIA</b>

<dd></dd>
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
<dt>D3dkmthk.h (include TBD)</dt>
</dl>
</td>
</tr>
</table>