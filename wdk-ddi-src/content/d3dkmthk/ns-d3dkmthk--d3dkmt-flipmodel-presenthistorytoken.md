---
UID: NS.d3dkmthk._D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN
title: D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN
author: windows-driver-content
description: The D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN structure identifies a flip present-history operation.
old-location: display\d3dkmt_flipmodel_presenthistorytoken.htm
old-project: display
ms.assetid: dcf844e3-3346-485e-8965-c8cb824e2c78
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN, D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN is Supported starting with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN
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

# D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN structure



## -description
<p>The D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN structure identifies a flip present-history operation.</p>


## -syntax

````
typedef struct _D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN {
  UINT64                                    FenceValue;
  ULONG64                                   hLogicalSurface;
  UINT                                      SwapChainIndex;
  UINT64                                    PresentLimitSemaphoreId;
  D3DDDI_FLIPINTERVAL_TYPE                  FlipInterval;
  D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS Flags;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
  LONG64                                    hCompSurf;
  UINT64                                    CompositionSyncKey;
  UINT                                      RemainingTokens;
  RECT                                      ScrollRect;
  POINT                                     ScrollOffset;
  UINT                                      PresentCount;
  FLOAT                                     RevealColor[4];
  D3DDDI_ROTATION                           Rotation;
  D3DKMT_SCATTERBLTS                        ScatterBlts;
  D3DKMT_HANDLE                             hSyncObject;
#endif 
  D3DKMT_DIRTYREGIONS                       DirtyRegions;
} D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN;
````


## -struct-fields
<dl>

### -field <b>FenceValue</b>

<dd>
<p>[in] A 64-bit value that specifies the fence value that is used for the flip.</p>
</dd>

### -field <b>hLogicalSurface</b>

<dd>
<p>[in] A 64-bit value that specifies the handle to a logical surface.</p>
</dd>

### -field <b>SwapChainIndex</b>

<dd>
<p>[in] The index of the surface in the swap chain that is used for the flip.</p>
</dd>

### -field <b>PresentLimitSemaphoreId</b>

<dd>
<p>[in] A 64-bit value that identifies the present-limit semaphore.</p>
</dd>

### -field <b>FlipInterval</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544549">D3DDDI_FLIPINTERVAL_TYPE</a>-typed value that indicates the flip interval (that is, if the flip occurs after zero, one, two, three, or four vertical syncs).</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff547991">D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS</a> structure that identifies, in bit-field flags, attributes of a flip present-history operation.</p>
</dd>

### -field <b>hCompSurf</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>CompositionSyncKey</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>RemainingTokens</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>ScrollRect</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>ScrollOffset</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>PresentCount</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>RevealColor</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>Rotation</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>ScatterBlts</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>hSyncObject</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>DirtyRegions</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff547937">D3DKMT_DIRTYREGIONS</a> structure that identifies the active rectangles (dirty regions) of the flip surface.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN is Supported starting with the Windows 7 operating system. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544549">D3DDDI_FLIPINTERVAL_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547937">D3DKMT_DIRTYREGIONS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547991">D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548188">D3DKMT_PRESENTHISTORYTOKEN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
