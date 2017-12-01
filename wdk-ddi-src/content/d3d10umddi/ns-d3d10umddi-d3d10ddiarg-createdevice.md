---
UID: NS.d3d10umddi.D3D10DDIARG_CREATEDEVICE
title: D3D10DDIARG_CREATEDEVICE
author: windows-driver-content
description: The D3D10DDIARG_CREATEDEVICE structure describes the display device to create.
old-location: display\d3d10ddiarg_createdevice.htm
old-project: display
ms.assetid: 64154d8a-1775-455b-bf31-9c3a0f1398ad
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D10DDIARG_CREATEDEVICE, D3D10DDIARG_CREATEDEVICE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10DDIARG_CREATEDEVICE
req.alt-loc: d3d10umddi.h
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

# D3D10DDIARG_CREATEDEVICE structure



## -description
<p>The <b>D3D10DDIARG_CREATEDEVICE</b> structure describes the display device to create.</p>


## -syntax

````
typedef struct D3D10DDIARG_CREATEDEVICE {
  D3D10DDI_HRTDEVICE            hRTDevice;
  UINT                          Interface;
  UINT                          Version;
  const D3DDDI_DEVICECALLBACKS  *pKTCallbacks;
  union {
    D3D10DDI_DEVICEFUNCS      *pDeviceFuncs;
#if D3D10DDI_MINOR_HEADER_VERSION >= 1 || D3D11DDI_MINOR_HEADER_VERSION >= 1
    D3D10_1DDI_DEVICEFUNCS    *p10_1DeviceFuncs;
#endif 
#if D3D11DDI_MINOR_HEADER_VERSION >= 1
    D3D11DDI_DEVICEFUNCS      *p11DeviceFuncs;
#endif 
#if D3D11DDI_MINOR_HEADER_VERSION >= 3
    D3D11_1DDI_DEVICEFUNCS    *p11_1DeviceFuncs;
#endif 
#if D3D11DDI_MINOR_HEADER_VERSION >= 4
    D3DWDDM1_3DDI_DEVICEFUNCS *pWDDM1_3DeviceFuncs;
#endif 
  };
  D3D10DDI_HDEVICE              hDrvDevice;
  DXGI_DDI_BASE_ARGS            DXGIBaseDDI;
  D3D10DDI_HRTCORELAYER         hRTCoreLayer;
  union {
    const D3D10DDI_CORELAYER_DEVICECALLBACKS *pUMCallbacks;
#if D3D11DDI_MINOR_HEADER_VERSION >= 1
    const D3D11DDI_CORELAYER_DEVICECALLBACKS *p11UMCallbacks;
#endif 
  };
  UINT                          Flags;
#if D3D11DDI_MINOR_HEADER_VERSION >= 3
  PFND3D10DDI_RETRIEVESUBOBJECT *ppfnRetrieveSubObject;
#endif 
} D3D10DDIARG_CREATEDEVICE;
````


## -struct-fields
<dl>

### -field <b>hRTDevice</b>

<dd>
<p>[in] A handle to the display device (graphics context) that specifies the handle that the driver should use when it calls back into the Direct3D runtime (that is, when the driver calls functions that the <b>pKTCallbacks</b> member specifies). </p>
</dd>

### -field <b>Interface</b>

<dd>
<p>[in] The Direct3D interface version. The high 16 bits store the major release number (such as 10, 11, and so on); the low 16 bits store the minor release number (such as 0, 1, 2, and so on). The minor release number will be increased when a change to the interface is released.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>[in] A number that the driver can use to identify when the Direct3D runtime was built. The high 16 bits represent the build number; the low 16 bits represent the revision number. </p>
<p>The driver is required only to monitor the high 16 bits. The driver should ensure that the runtime build version that is passed in is greater than or equal to the current build version of the driver. The driver should return a failure from its <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a> function if the passed in build version is incompatible. </p>
</dd>

### -field <b>pKTCallbacks</b>

<dd>
<p>[in] A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddi-devicecallbacks.md">D3DDDI_DEVICECALLBACKS</a> structure that contains a table of Direct3D runtime callback functions that the driver can use to access kernel services.</p>
</dd>

### -field <b>pDeviceFuncs</b>

<dd>
<p>[in/out] A pointer to a <a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi-devicefuncs.md">D3D10DDI_DEVICEFUNCS</a> structure that the user-mode display driver fills with a table of its functions. The Direct3D runtime uses these functions to communicate with the user-mode display driver.</p>
<p>The driver should fill its Direct3D version 10.0 functions in the supplied <a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi-devicefuncs.md">D3D10DDI_DEVICEFUNCS</a> structure when the value in the <b>Interface</b> member is <b>D3D10_0_DDI_INTERFACE_VERSION</b>.  </p>
</dd>

### -field <b>p10_1DeviceFuncs</b>

<dd>
<p>[in/out] A pointer to a <a href="..\d3d10umddi\ns-d3d10umddi-d3d10-1ddi-devicefuncs.md">D3D10_1DDI_DEVICEFUNCS</a> structure that the user-mode display driver fills with a table of its functions. Version 10.1 of the Direct3D runtime uses these functions to communicate with the user-mode display driver.</p>
<p>The driver should fill its Direct3D version 10.1 functions in the supplied <a href="..\d3d10umddi\ns-d3d10umddi-d3d10-1ddi-devicefuncs.md">D3D10_1DDI_DEVICEFUNCS</a> structure when the value in the <b>Interface</b> member is <b>D3D10_1_DDI_INTERFACE_VERSION</b>. </p>
<p>Supported starting with Windows Vista with SP1 and Windows Server 2008.</p>
</dd>

### -field <b>p11DeviceFuncs</b>

<dd>
<p>[in/out] A pointer to a <a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi-devicefuncs~r1.md">D3D11DDI_DEVICEFUNCS</a> structure that the user-mode display driver fills with a table of its functions. Version 11 of the Direct3D runtime uses these functions to communicate with the user-mode display driver.</p>
<p>The driver should fill its Direct3D version 11.0 functions in the supplied <a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi-devicefuncs~r1.md">D3D11DDI_DEVICEFUNCS</a> structure when the value in the <b>Interface</b> member is <b>D3D11_0_DDI_INTERFACE_VERSION</b>.  </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>p11_1DeviceFuncs</b>

<dd>
<p>[in/out] A pointer to a <a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-devicefuncs~r1.md">D3D11_1DDI_DEVICEFUNCS</a> structure that the user-mode display driver fills with a table of its functions. Starting with version 11.1, the Direct3D runtime uses these functions to communicate with the user-mode display driver.</p>
<p>The driver should fill its Direct3D version 11.1 functions in the supplied <a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-devicefuncs~r1.md">D3D11_1DDI_DEVICEFUNCS</a> structure when the value in the <b>Interface</b> member is <b>D3D11_1_DDI_INTERFACE_VERSION</b>.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>pWDDM1_3DeviceFuncs</b>

<dd>
<p>[in/out] A pointer to a <a href="..\d3d10umddi\ns-d3d10umddi-d3dwddm1-3ddi-devicefuncs~r1.md">D3DWDDM1_3DDI_DEVICEFUNCS</a> structure that the user-mode display driver fills with a table of its functions. Version 11.2 of the Direct3D runtime uses these functions to communicate with the user-mode display driver.</p>
<p>The driver should fill its Direct3D version 11.2 functions in the supplied <a href="..\d3d10umddi\ns-d3d10umddi-d3dwddm1-3ddi-devicefuncs~r1.md">D3DWDDM1_3DDI_DEVICEFUNCS</a> structure when the value in the <b>Interface</b> member is <b>D3DWDDM1_3_DDI_INTERFACE_VERSION</b>.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>hDrvDevice</b>

<dd>
<p>[in/out] A handle to the display device (graphics context) that the Direct3D runtime uses in subsequent driver calls to identify the display device.</p>
</dd>

### -field <b>DXGIBaseDDI</b>

<dd>
<p>[in/out] A <a href="..\dxgiddi\ns-dxgiddi-dxgi-ddi-base-args.md">DXGI_DDI_BASE_ARGS</a> structure that provides access to the DXGI. The DXGI DDI handles low-level tasks like presenting rendered frames to an output, controlling gamma, and managing a full-screen transition. </p>
</dd>

### -field <b>hRTCoreLayer</b>

<dd>
<p>[in] A handle that the driver should use when it calls back into the Direct3D runtime to access core Direct3D 10 functionality (that is, when the driver calls functions that the <b>pUMCallbacks</b> member specifies). </p>
</dd>

### -field <b>pUMCallbacks</b>

<dd>
<p>[in] A pointer to a <a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi-corelayer-devicecallbacks.md">D3D10DDI_CORELAYER_DEVICECALLBACKS</a> structure that contains a table of Direct3D 10 runtime callback functions that the driver can use to access core user-mode runtime functionality. </p>
</dd>

### -field <b>p11UMCallbacks</b>

<dd>
<p>[in] A pointer to a <a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi-corelayer-devicecallbacks~r1.md">D3D11DDI_CORELAYER_DEVICECALLBACKS</a> structure that contains a table of Direct3D 11 runtime callback functions, which the driver can use to access core user-mode runtime functionality.</p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A valid bitwise OR of flag values that identify how to create the display device. The Direct3D runtime supports the following flags:  </p>
<p></p>
<dl>

### -field <a id="D3D10DDI_CREATEDEVICE_FLAG_DISABLE_EXTRA_THREAD_CREATION__0x1__"></a><a id="d3d10ddi_createdevice_flag_disable_extra_thread_creation__0x1__"></a><a id="D3D10DDI_CREATEDEVICE_FLAG_DISABLE_EXTRA_THREAD_CREATION__0X1__"></a>D3D10DDI_CREATEDEVICE_FLAG_DISABLE_EXTRA_THREAD_CREATION (0x1) 

<dd>
<p>If this flag is set, the user-mode display driver should not run multiple threads simultaneously when it processes calls to its functions from the Direct3D runtime. A driver can typically start and run multiple threads to process operations faster, unless the <b>D3D10DDI_CREATEDEVICE_FLAG_DISABLE_EXTRA_THREAD_CREATION</b> flag is set.</p>
</dd>

### -field <a id="D3D11DDI_CREATEDEVICE_FLAG_SINGLETHREADED__0x10__"></a><a id="d3d11ddi_createdevice_flag_singlethreaded__0x10__"></a><a id="D3D11DDI_CREATEDEVICE_FLAG_SINGLETHREADED__0X10__"></a>D3D11DDI_CREATEDEVICE_FLAG_SINGLETHREADED (0x10) 

<dd>
<p>This flag informs the user-mode display driver that the application is single threaded. The Direct3D 11 runtime allows multiple application threads to enter the driver if the driver allows this mode of operation. However, not all applications can run multiple threads. If this flag is set, the driver does not expect multiple threads to enter it and run simultaneously. The driver can avoid synchronization if this flag is set.</p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <a id="The_flag_that_is_set_in_the_0xE_mask_of_the_Flags_member"></a><a id="the_flag_that_is_set_in_the_0xe_mask_of_the_flags_member"></a><a id="THE_FLAG_THAT_IS_SET_IN_THE_0XE_MASK_OF_THE_FLAGS_MEMBER"></a>The flag that is set in the 0xE mask of the <b>Flags</b> member

<dd>
<p>This flag represents the level of 3-D pipeline that the driver should support for the display device. The driver uses the following constant and macros to extract one of the values from the <a href="..\d3d10umddi\ne-d3d10umddi-d3d11ddi-3dpipelinelevel.md">D3D11DDI_3DPIPELINELEVEL</a> enumeration that represent the 3-D pipeline level to support. The value in the <b>Flags</b> member is formatted like the <b>Caps</b> member of the <a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi-3dpipelinesupport-caps.md">D3D11DDI_3DPIPELINESUPPORT_CAPS</a> structure.</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>#define D3D11DDI_CREATEDEVICE_FLAG_3DPIPELINESUPPORT_SHIFT (0x1)
#define D3D11DDI_CREATEDEVICE_FLAG_3DPIPELINESUPPORT_MASK (0x7 &lt;&lt; D3D11DDI_CREATEDEVICE_FLAG_3DPIPELINESUPPORT_SHIFT)
#define D3D11DDI_EXTRACT_3DPIPELINELEVEL_FROM_FLAGS( Flags ) \
    ((D3D11DDI_3DPIPELINELEVEL)(((Flags) &amp; D3D11DDI_CREATEDEVICE_FLAG_3DPIPELINESUPPORT_MASK) &gt;&gt; \
    D3D11DDI_CREATEDEVICE_FLAG_3DPIPELINESUPPORT_SHIFT))</pre>
</td>
</tr>
</table></span></div>
<p>Supported starting with Windows 7.</p>
</dd>
</dl>
</dd>

### -field <b>ppfnRetrieveSubObject</b>

<dd>
<p>[in/out] A pointer to a <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-retrievesubobject.md">RetrieveSubObject(D3D11_1)</a> function that retrieves subparts of a Direct3D driver device object.</p>
<p>Supported starting with Windows 8.</p>
</dd>
</dl>

## -remarks
<p>The driver examines values in the <b>Interface</b> and <b>Version</b> members to determine whether to fill the <a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi-devicefuncs.md">D3D10DDI_DEVICEFUNCS</a>, <a href="..\d3d10umddi\ns-d3d10umddi-d3d10-1ddi-devicefuncs.md">D3D10_1DDI_DEVICEFUNCS</a>, <a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi-devicefuncs~r1.md">D3D11DDI_DEVICEFUNCS</a>, <a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-devicefuncs~r1.md">D3D11_1DDI_DEVICEFUNCS</a>, or <a href="..\d3d10umddi\ns-d3d10umddi-d3dwddm1-3ddi-devicefuncs~r1.md">D3DWDDM1_3DDI_DEVICEFUNCS</a> structure that the <b>pDeviceFuncs</b>, <b>p10_1DeviceFuncs</b>, <b>p11DeviceFuncs</b>, <b>p11_1DeviceFuncs</b>, or  <b>pWDDM1_3DeviceFuncs</b> member points to with the driver's functions. The following constants from D3d10umddi.h are examples of the constants that the driver might find in <b>Interface</b> and <b>Version</b>:</p>

<p>Other possible combinations of constants for different versions of the operating system, Direct3D, and Windows Display Driver Model (WDDM) are listed in the D3d10umddi.h header.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10-1ddi-devicefuncs.md">D3D10_1DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi-corelayer-devicecallbacks.md">D3D10DDI_CORELAYER_DEVICECALLBACKS</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi-corelayer-devicecallbacks~r1.md">D3D11DDI_CORELAYER_DEVICECALLBACKS</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi-devicefuncs.md">D3D10DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-devicefuncs~r1.md">D3D11_1DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="..\d3d10umddi\ne-d3d10umddi-d3d11ddi-3dpipelinelevel.md">D3D11DDI_3DPIPELINELEVEL</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi-3dpipelinesupport-caps.md">D3D11DDI_3DPIPELINESUPPORT_CAPS</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi-devicefuncs~r1.md">D3D11DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3dwddm1-3ddi-devicefuncs~r1.md">D3DWDDM1_3DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-allocationlist.md">D3DDDI_ALLOCATIONLIST</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddi-devicecallbacks.md">D3DDDI_DEVICECALLBACKS</a>
</dt>
<dt>
<a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-patchlocationlist.md">D3DDDI_PATCHLOCATIONLIST</a>
</dt>
<dt>
<a href="..\dxgiddi\ns-dxgiddi-dxgi-ddi-base-args.md">DXGI_DDI_BASE_ARGS</a>
</dt>
<dt>
<a href="display.dxgkddicreatedevice">DxgkDdiCreateDevice</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-retrievesubobject.md">RetrieveSubObject(D3D11_1)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10DDIARG_CREATEDEVICE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
