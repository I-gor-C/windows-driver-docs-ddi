---
UID: NS.d3d10umddi.D3D10DDIARG_CALCPRIVATEDEVICESIZE
title: D3D10DDIARG_CALCPRIVATEDEVICESIZE
author: windows-driver-content
description: The D3D10DDIARG_CALCPRIVATEDEVICESIZE structure describes the parameters that the user-mode display driver uses to calculate the size of a memory block that the driver requires to store frequently-accessed data.
old-location: display\d3d10ddiarg_calcprivatedevicesize.htm
old-project: display
ms.assetid: 79bb55db-dd4d-4cad-927e-e1126463bded
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D10DDIARG_CALCPRIVATEDEVICESIZE, D3D10DDIARG_CALCPRIVATEDEVICESIZE
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
req.alt-api: D3D10DDIARG_CALCPRIVATEDEVICESIZE
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

# D3D10DDIARG_CALCPRIVATEDEVICESIZE structure



## -description
<p>The D3D10DDIARG_CALCPRIVATEDEVICESIZE structure describes the parameters that the user-mode display driver uses to calculate the size of a memory block that the driver requires to store frequently-accessed data.</p>


## -syntax

````
typedef struct D3D10DDIARG_CALCPRIVATEDEVICESIZE {
  UINT Interface;
  UINT Version;
  UINT Flags;
} D3D10DDIARG_CALCPRIVATEDEVICESIZE;
````


## -struct-fields
<dl>

### -field <b>Interface</b>

<dd>
<p>[in] The Microsoft Direct3D interface version. The high 16 bits store the major release number (such as 10, 11, and so on); the low 16 bits store the minor release number (such as 0, 1, 2, and so on). The minor release number will be increased when a change to the interface is released.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>[in] A number that the driver can use to identify when the Direct3D runtime was built. The high 16 bits represent the build number; the low 16 bits represent the revision number. </p>
<p>The driver is required only to monitor the high 16 bits. The driver should ensure that the runtime build version that is passed in is greater than or equal to the current build version of the driver. The driver should return a failure from its <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivatedevicesize.md">CalcPrivateDeviceSize</a> function if the passed in build version is incompatible. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A valid bitwise OR of flag values that identify how to create a rendering device. The Direct3D runtime supports the following flags:  </p>
<p></p>
<dl>

### -field <a id="D3D10DDI_CREATEDEVICE_FLAG_DISABLE_EXTRA_THREAD_CREATION__0x1__"></a><a id="d3d10ddi_createdevice_flag_disable_extra_thread_creation__0x1__"></a><a id="D3D10DDI_CREATEDEVICE_FLAG_DISABLE_EXTRA_THREAD_CREATION__0X1__"></a>D3D10DDI_CREATEDEVICE_FLAG_DISABLE_EXTRA_THREAD_CREATION (0x1) 

<dd>
<p>If this flag is set, the user-mode display driver should not run multiple threads simultaneously when it processes calls to its functions from the Direct3D runtime. A driver can typically start and run multiple threads to process operations faster, unless the D3D10DDI_CREATEDEVICE_FLAG_DISABLE_EXTRA_THREAD_CREATION flag is set.</p>
</dd>

### -field <a id="D3D11DDI_CREATEDEVICE_FLAG_SINGLETHREADED__0x10__"></a><a id="d3d11ddi_createdevice_flag_singlethreaded__0x10__"></a><a id="D3D11DDI_CREATEDEVICE_FLAG_SINGLETHREADED__0X10__"></a>D3D11DDI_CREATEDEVICE_FLAG_SINGLETHREADED (0x10) 

<dd>
<p>Supported in Windows 7 and later versions. </p>
<p>This flag informs the user-mode display driver that the application is single threaded. The Direct3D version 11 runtime allows multiple application threads to enter the driver if the driver allows this mode of operation. However, not all applications can run multiple threads. If this flag is set, the driver does not expect multiple threads to enter it and run simultaneously. The driver can avoid synchronization if this flag is set.</p>
</dd>

### -field <a id="The_flag_that_is_set_in_the_0xE_mask_of_the_Flags_member_"></a><a id="the_flag_that_is_set_in_the_0xe_mask_of_the_flags_member_"></a><a id="THE_FLAG_THAT_IS_SET_IN_THE_0XE_MASK_OF_THE_FLAGS_MEMBER_"></a>The flag that is set in the 0xE mask of the <b>Flags</b> member 

<dd>
<p>Supported in Windows 7 and later versions. </p>
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
</dd>
</dl>
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
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-calcprivatedevicesize.md">CalcPrivateDeviceSize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10DDIARG_CALCPRIVATEDEVICESIZE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
